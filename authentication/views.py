from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
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
            fname = user.first_name
            return render(request, 'home.html', {'fname': fname})
            # return redirect('home')
        else:
            messages.error(request, "Bad Credentials!")
            # return HttpResponse("bad credentials")
            return redirect('login')

    return render(request,'authentication/login.html')
    
def signup(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST['email']
        rollno = request.POST["rollno"]
        username = request.POST['username']
        passwd = request.POST["passwd"]


        myuser = User.objects.create_user(fname, email, passwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.email = email
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        # messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        return redirect('login')    
    return render(request, 'authentication/signup.html')