from django.contrib import admin
from .models import Product,ToysList,SchoolList,MyOrders,Address,Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(ToysList)
admin.site.register(SchoolList)
admin.site.register(MyOrders)
admin.site.register(Address)
admin.site.register(Cart)
