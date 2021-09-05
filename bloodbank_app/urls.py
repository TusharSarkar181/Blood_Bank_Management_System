from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('',views.indexView, name='index'),
    path('index',views.indexView, name='index'),
    path('home.html',views.homeView, name='home'),
    path('login.html',views.loginView, name='login'),
    path('register.html',views.registerView, name='register'),
    path('about.html',views.aboutView, name='about'),
    path('contact.html',views.contactView, name='contact'),
    path('specialservices.html',views.specialservicesView, name='specialservices'),
    path('PaymentGateway.html',views.PaymentGatewayView, name='PaymentGateway'),
    path('DonorDetails.html',views.DonorDetailsView, name='DonorDetails'),
    path('DonorRegistration.html',views.DonorRegistrationView, name='DonorRegistration'),
    path('search', views.search_result, name='search'),




]