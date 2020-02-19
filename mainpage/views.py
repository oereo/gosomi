from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.

def home(request):
    user = request.user
    if request.method == "POST":
        username = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print(user.username + " userid")
            return redirect('/',user)
        else:
            return render(request, 'home.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'home.html')

def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return redirect('/')
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')