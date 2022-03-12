from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def homePageRender(request):
    context = {}
    return render(request, 'users/home_page.html', context)



def loginUser(request):
    if request.user.is_authenticated:
        return redirect('mynotes')
    
    print("Getting login form...")
    print("Checking if method is POST...")
    if request.method == "POST":
        print("Method is post")
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'USERNAME DOES NOT EXIST')

        # QUERYING THE DATABASE
        user = authenticate(request, username=username, password=password)
        print("Authenticating...")

        # login FUNCTION CREATES SESSION FOR THE USER
        if user is not None:
            login(request, user)
            return render(request, 'notes/notes.html')
            # return redirect(request.GET['next'] if 'next' in request.GET else 'notes')
        else:
            print("No you don't exist..")
            messages.error(request, "USERNAME OR PASSWORD IS INCORRECT")
            return redirect('login')
    else:
        print("Redirecting back to login form...")
        return render(request, 'users/login_form.html')


    # return render(request, 'users/login_form.html')


@login_required
def logoutUser(request):
    print("Logging user out...")
    logout(request)
    messages.info(request, 'USER WAS LOGGED OUT')
    return render(request, 'users/home_page.html')

