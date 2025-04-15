from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path ('About/',views.About, name='About'),
    path ('Contact/', views.Contact, name='Contact'),
    path ('Privacy/', views.Privacy, name='Privacy'),
    path ('Terms/', views.Terms, name='Terms'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),



]

