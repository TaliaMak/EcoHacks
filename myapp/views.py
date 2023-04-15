from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import User


def login(request):
    model = User
    return render(request, 'myapp/login.html')

def login_reroute(request):
    users = User.objects.all()
    usern = request.POST.get("username", False)
    password1 = request.POST.get("password", False)
    if users.all().filter(username = usern) and users.all().get(username = usern).password == password1:
        return HttpResponseRedirect(reverse('account'))
        #return render(request, 'myapp/account.html')
    else:
        return render(request, 'myapp/login_reroute.html') # this page is to say password or username is incorrect



def account(request):
    model = User
    return render(request, 'myapp/account.html')


def create_account(request):
    model = User
    return render(request, 'myapp/create_account.html')


def reroute_create_account(request):
    model = User

    # according to this reference, https://docs.djangoproject.com/en/4.2/topics/auth/default/:
    #comes with username, email, password, first_name, and last_name field
    usern = request.POST.get("username", False)
    email = request.POST.get("email", False)
    password = request.POST.get("password", False)
    user1 = User()
    user1.username = usern
    user1.email = email
    user1.password = password
    user1.first_name = request.POST.get("first_name", False)
    user1.last_name = request.POST.get("last_name", False)
    user1.save()
    return render(request, 'myapp/created_account.html')
def created_account(request):
    model = User
    return render(request, 'myapp/created_account.html')

def calculate_reroute(request):
    value = request.POST.get('Radio', 'Food')
    
    return render(request, f'myapp/{value}.html')

def food(request):
    pass

def goods(request):
    pass

def transportation(request):
    pass




