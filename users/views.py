from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginUser(request):
    page = 'register'
    
    if request.user.is_authenticated:
        return redirect('notes')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'USERNAME DOES NOT EXIST')

        # QUERYING THE DATABASE
        user = authenticate(request, username=username, password=password)

        # login FUNCTION CREATES SESSION FOR THE USER
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else'notes')
        else:
            messages.error(request, "USERNAME OR PASSWORD IS INCORRECT")

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'USER WAS LOGGED OUT')
    return redirect('login')