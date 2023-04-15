from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import User


def login(request):
    model = User
    return render(request, 'myapp/login.html')



