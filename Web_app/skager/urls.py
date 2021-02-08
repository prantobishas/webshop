from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alle_producten/', views.all_products, name='all_products'),
    path('producten/<str:category>/', views.product, name='product'),
    path('details/<str:category>/<str:name>/', views.details, name='details'),
    path('toevoegen/<str:category>/<str:name>/<str:price_one>/<str:page>/', views.add, name='add'),
    path('verwijder/<str:name>/', views.delete, name='delete'),
    path('verwijder_allen/<str:name>/', views.delete_all, name='delete_all'),
    path('bericht/<str:category>/', views.message, name='message'),
    path('winkelwagen/', views.cart, name='cart'),
    path('geld_versturen/', views.money, name='money'),
    path('geld_versturen2/', views.money2, name='money2'),
    path('stel_vraag/', views.ask, name='ask'),
    path('adres/', views.address, name='address'),
    path('adres2/', views.address2, name='address2'),
    path('<str:string>/', views.error, name='error'),
] 