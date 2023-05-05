from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def aboutUs(request):
    return render(request, 'aboutUs.html')

def home(request):
    return render(request, 'home.html')

def bye(request):
    return HttpResponse("bye bye")

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']

        user = authenticate(username=username, password= passwd)
        
        if user is not None:
            login(request ,user)
            username = user.username
            return render(request, 'home.html', {'username': username})
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!")
            # return HttpResponse("bad credentials")
            return redirect('signin')

    return render(request,'authentication/login.html')
    
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST["passwd"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST['email']
        rollno = request.POST["rollno"]


        myuser = User.objects.create_user(username, email, passwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.email = email
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        # messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        return redirect('signin')    
    return render(request, 'authentication/signup.html')