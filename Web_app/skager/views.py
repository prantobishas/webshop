#######################################################################################
#  views.py
#
#  Minor programmeren - Web App Studio.
#
#  Pranto Bishas.
#  20 years old and lives in the Netherlands.
#  Studies Medical Science at VU Amsterdam.
#
#  This program implements functions based on django to make a webshop of a store. 
#  The user will be directed to the homepage, where the user can search for a 
#  product and add it to the shoppingcart, when logged in. When placing orders the 
#  user has to provide his/her address and will get a confirmation mail afterwards.
#  The site also contains a foreign exchange calculator, because the store contains
#  a moneytransfer service. In the footer the user can submit a question to the admin.
#
#  Demonstrates use of django and API.
########################################################################################


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Count, Sum
from django.core.mail import send_mail
import requests
from .models import Product,ToysList,SchoolList,MyOrders,Address,Cart

# Render homepage, while checking if user is logged in.
def home(request):
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "Categories": get_categories(request),
    }
    return render(request, 'skager/homepage.html', context)

# Render page with all the products.
def all_products(request):
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "ProductList": Product.objects.order_by('name'),
        "Categories": get_categories(request),
    }

    # If user is searching a query.
    if request.method == 'POST':

        # Get value of query by name.
        query = request.POST['query']

        # Filter all products with the query in the name 
        # and update values in the context dictionary.
        context["ProductList"] = Product.objects.filter(name__icontains=query) \
                                    .order_by('name')
        context["Query"] = query
        context["Count"] = Product.objects.filter(name__icontains=query).count()
    
    return render(request, 'skager/allproducts.html', context)

# Render page with the products corresponding to the given category.
def product(request,category):
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "ProductList": Product.objects.filter(category=category).order_by('name'),
        "Categories": get_categories(request),
        "CurrentCat": category
    }
    return render(request, 'skager/products.html', context)

# Render page with product details.
def details(request,category,name):
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "ProductList": Product.objects.filter(category=category).order_by('name'),
        "CurrentCat": category,
        "Product": Product.objects.filter(name=name),
        "Categories": get_categories(request),
        "Name": name,
    }
    return render(request, 'skager/details.html', context)

# Adding items to the shoppingcart.
def add(request,category,name,price_one,page):

    # If product is already in the Cart model.
    if Cart.objects.filter(user=request.user,name=name).count() > 0:
        product = Cart.objects.get(user=request.user,name=name)

        # Increase amount by 1 and update the price for that amount.
        product.amount += 1
        product.price_many += product.price_one
        product.save()

    # If product is not in the shoppingcart.
    else:

        # Add a new object with the given values. 
        add = Cart(user=request.user,category=category,name=name, \
                    amount=1,price_one=price_one,price_many=price_one) 
        add.save()

    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "ProductList": Product.objects.filter(category=category).order_by('name'),
        "CurrentCat": category,
        "Product": Product.objects.filter(name=name),
        "Categories": get_categories(request),
        "Name": name,
        "Amount": Cart.objects.get(user=request.user,name=name).amount,
        "Message": "is toegevoegd aan mijn winkelwagen",
    }

    # Render the page where the user is currently on.
    if page == 'allproducts':
        context["ProductList"] = Product.objects.all().order_by('name')
        return render(request, 'skager/allproducts.html', context)
    elif page == 'products':
        return render(request, 'skager/products.html', context)
    elif page == 'details':
        return render(request, 'skager/details.html', context)

# Delete items from shoppingcart.
def delete(request,name):

    # Get the right product.
    cart_item = Cart.objects.get(user=request.user,name=name)

    # If there is only one amount of the product, delete the object.
    if cart_item.amount == 1:
        cart_item.delete()

    # Else decrease amount by 1 and update the price.
    else:
        cart_item.amount -= 1
        cart_item.price_many -= cart_item.price_one
        cart_item.save()
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "Cart": Cart.objects.filter(user=request.user).order_by('name'),
        "Address": Address.objects.filter(user=request.user),
        "Categories": get_categories(request),
        "Name": name,
        "Total": get_total(request),
        "Message": "is verwijderd uit mijn winkelwagen",
    }
    return render(request, 'skager/cart.html', context)

# Delete the whole object of the product.
def delete_all(request,name):
    cart_item = Cart.objects.get(user=request.user,name=name)
    cart_item.delete()
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "Cart": Cart.objects.filter(user=request.user).order_by('name'),
        "Address": Address.objects.filter(user=request.user),
        "Categories": get_categories(request),
        "Name": name,
        "Total": get_total(request),
        "Message": "is verwijderd uit mijn winkelwagen",
    }
    return render(request, 'skager/cart.html', context)

# Render the page wich displays the shoppingcart of the user.
def cart(request):
    
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),

        # Filter the shoppingcart by the current user.
        "Cart": Cart.objects.filter(user=request.user).order_by('name'),
        "Address": Address.objects.filter(user=request.user),
        "Categories": get_categories(request),
        "Total": get_total(request),
    }
    
    # If the user is trying to place their order.
    if request.method == 'POST':

        # If the user has not given their address, render page to submit address.
        if Address.objects.filter(user=request.user).count() == 0:
            return redirect ('address')

        cart = Cart.objects.filter(user=request.user)

        # Make new object for the user.
        new = MyOrders(user=request.user)
        new.save()

        # For each order in the cart, add it to the many-to-many-field 'order'.
        for orders in cart:
            new.order.add(orders)
            new.save()

        # Retrieve strings for the confirmation email.
        subject = "Bevestiging bestelling bij Skagermultishop"
        message = "Uw bestelling is succesvol verwerkt:\n"

        # Get the last ordered order. 
        send_orders = MyOrders.objects.filter(user=request.user)[0]

        # Add each string-representation of the order to message.
        for orders in send_orders.order.all():
            message += f"{orders}\n"

        # Add totalprice and mail-footer.
        message += f"Totaal bedrag = € {get_total(request)} \
        \n\n Wij bedanken u voor uw bestelling.\n\n Met vriendelijke groeten, \
        \n\n Skagermultishop\n\n Skagerrak 210\n 2133DW Hoofddorp \
        \n skagermultishop@live.nl\n 023-5631305\n"
        
        from_email = 'pranto.django@gmail.com'

        # Send mail from the admin to the current user.
        send_mail(subject,message,from_email,[request.user.email],
        fail_silently=True)

        context["Message"] = "Uw bestelling is geplaatst. \
                                Bekijk uw email voor de bevestiging."
        return render(request, 'skager/succes.html', context)
    
    return render(request, 'skager/cart.html', context)

# Render page to add an address to the user.
def address(request):
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "Categories": get_categories(request),
    }

    # When submitting the address.
    if request.method == 'POST':
        street = request.POST['street']
        number = request.POST['number']
        zipcode = request.POST['zipcode']
        city = request.POST['city']

        # Add object of the user and the given address to the Address model.
        add = Address(user=request.user,street=street, \
                        number=number,zipcode=zipcode,city=city)
        add.save()
        return redirect('cart')

    return render(request, 'skager/adres.html', context)

# When user is changing address.
def address2(request):

    # Delete the current address and redirect to page for submitting addres.
    address = Address.objects.filter(user=request.user)[0]
    address.delete()
    return redirect ('address')

# Calculate foreign exchanges with EUR as base.
def money(request):

    # Get json response of the API with unique access-key.
    url = 'http://data.fixer.io/api/latest? \
            access_key=5994822a63a502c5b6ad2597e876744a'    
    req = requests.get(url)
    response = req.json()

    # Retrieve keys of the dictionary 'rates' from the API.
    currencies = response["rates"].keys()
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "Categories": get_categories(request),
        "saved_amount": "0.00",
        "Currency": currencies,
    }

    # When calculating.
    if request.method == 'POST':
        amount = request.POST["amount"]
        to_currency = request.POST["to_currency"]

        # Check for valid input.
        if amount == '' or float(amount) <= 0:
            context["Message"] = 'Voer alstublieft een geldig bedrag in'
        
        # If input is valid.
        else:

            # Get exchange-rate of given to_currency.
            rate = response["rates"][to_currency]

            # calculate exchange and display it with two decimal places.
            recieve = float(amount) * float(rate)
            recieve = "{0:.2f}".format(recieve)
            
            # Update values.
            context["Rate"] = rate
            context["saved_amount"] = amount
            context["to_currency"] = to_currency
            context["Receive"] = recieve
            context["Currency"] = currencies
    
    return render(request, 'skager/money.html', context)

# Calculate exchanges with the given foreign exchange as base.
def money2(request):

    # Get access to API.
    url = 'http://data.fixer.io/api/latest? \
            access_key=5994822a63a502c5b6ad2597e876744a'    
    req = requests.get(url)
    response = req.json()
    currencies = response["rates"].keys()
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "Categories": get_categories(request),
        "saved_amount": "0.00",
        "Currency": currencies,
    }

    # When calculating.
    if request.method == 'POST':
        amount = request.POST["amount"]
        from_currency = request.POST["from_currency"]

        # Check validation and calculate exchange.
        if amount == '' or float(amount) <= 0:
            context["Message"] = 'Voer alstublieft een geldig bedrag in'
        else:
            rate = response["rates"][from_currency]
            recieve = float(amount) / float(rate)
            recieve = "{0:.2f}".format(recieve)
            context["Rate"] = rate
            context["saved_amount"] = amount
            context["from_currency"] = from_currency
            context["Receive"] = recieve
            context["Currency"] = currencies

    return render(request, 'skager/money2.html', context)

# Ask-forum in footer.
def ask(request):

    # When submitting question.
    if request.method == 'POST':
        context = {
            "User": user_login(request),
            "ToysList": ToysList.objects.all(),
            "SchoolList": SchoolList.objects.all(),
            "Categories": get_categories(request),
            "Message": 'Uw bericht is verstuurd. \
                        Er wordt zo spoedig mogelijk antwoord gegeven.',
        }
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        question = request.POST['question']

        # Check validation.
        if question == '':
            context["Message"] = 'Uw bericht heeft een inhoud nodig om \
                te kunnen versturen. Dien uw bericht opnieuw in.'
            return render(request, 'skager/homepage.html', context)

        # Send question to the admin.
        subject = f"{subject}"
        message = f"Bericht ontvangen van: {name} - {email}\n\n \
                        Inhoud: \n {question}"
        from_email = 'pranto.django@gmail.com'
        send_mail(subject,message,from_email,[from_email],
        fail_silently=False)
    
    return render(request, 'skager/homepage.html', context)

# Gives message to the user on the current page 
# to login before adding items to the shoppingcart.
def message(request,category):
    context = {
        "User": user_login(request),
        "ToysList": ToysList.objects.all(),
        "SchoolList": SchoolList.objects.all(),
        "ProductList": Product.objects.filter(category=category).order_by('name'),
        "Categories": get_categories(request),
        "CurrentCat": category,
        "Message1": 'Voor het toevoegen van producten, moet u ingelogd zijn. Klik',
        "Message2": 'hier',
        "Message3": 'om in te loggen.',
    }
    if category == 'allproducts':
        context["ProductList"] = Product.objects.all()
        return render(request, 'skager/allproducts.html', context)
    
    return render(request, 'skager/products.html', context)

# Return error-page if user is trying a invalid get request.
def error(request,string):
    return render(request, 'skager/error.html', 
        {"Message": 'Pagina 404 - Deze pagina bestaat niet'})

# Check if user is logged in.
def user_login(request):
    user = False
    if request.user.is_authenticated:
        user = True        
    return user

# Get total price of the products in the shoppingcart.
def get_total(request):
    total = None
    if Cart.objects.filter(user=request.user).count() > 0:
        dic_total = Cart.objects.filter(user=request.user) \
                        .aggregate(Sum('price_many'))
        total = "{0:.2f}".format(dic_total["price_many__sum"])        
    return total

# Get all the categories listed in the footer.
def get_categories(request):
    categories = []
    for cat in Product.CATEGORIES:
        categories.append(cat[0])
    return categories

