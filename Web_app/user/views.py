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
#  This file is for the registration, login and logout of the user.
#
#  Demonstrates use of django.
########################################################################################


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def login_view(request):

    # When the user is trying to login.
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if user is already registered.
        user = authenticate(request, username=username, password=password)

        # If user exist, continue to homepage.
        if user is not None:
            login(request, user)
            return redirect('home')
        
        # Else provide suiting message.
        else:
            return render(request, "user/login.html", {"Message": "Gebruikersnaam en/of wachtwoord komen niet overeen."})
    return render(request, 'user/login.html')

def register_view(request):

    # Default values for username and email.
    context = {
        "SavedName": "",
        "SavedEmail": "",
    }

    # If user is trying to registrate
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Check if username is already taken.
        if User.objects.filter(username=username).count() > 0:
            context = {
                "SavedName": username,
                "SavedEmail": email,
                "Message": "Gebruikersnaam is al in gebruik.",
            }
            return render(request, "user/registration.html", context)

        # Check if email is kind of valid.
        elif '@' not in email:
            context = {
                "SavedName": username,
                "SavedEmail": email,
                "Message": "E-mail is ongeldig.",
            }
            return render(request, "user/registration.html", context)

        # Check if the repeated password is the same as the original.
        elif password1 != password2:
            context = {
                "SavedName": username,
                "SavedEmail": email,
                "Message": "Wachtwoorden kwamen niet overeen.",
            }
            return render(request, "user/registration.html", context)

        # Check if the password is at least 8 characters.
        elif len(password1) < 8:
            context = {
                "SavedName": username,
                "SavedEmail": email,
                "Message": "Wachtwoord is te kort.",
            }
            return render(request, "user/registration.html", context)

        # Check if username and password aren't the same.
        elif username == password1:
            context = {
                "SavedName": username,
                "SavedEmail": email,
                "Message": "Wachtwoord en gebruikersnaam mogen niet overeenkomen.",
            }
            return render(request, "user/registration.html", context)

        # If user passed the validations, create user and redirect to login.
        else:
            User.objects.create_user(username=username,password=password1,email=email)
            return redirect('login')
    return render(request, "user/registration.html", context)        

def logout_view(request):

    # Logout user and return the homepage.
    logout(request)
    return redirect('home')