"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("/reroute", views.login_reroute, name = "login_reroute"),
    path("/account", views.account, name="account"),
    path("/createaccount", views.create_account, name = "create_account"),
    path("/createaccount/reroute", views.reroute_create_account, name = "reroute_create_account"),
    path("/createaccount/createdaccount", views.created_account, name="created_account"),
]
