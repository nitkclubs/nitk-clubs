from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Student

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

        else:
            messages.warning(request, "Bad Credentials!")

    return render(request,'authentication/login.html')
    
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST["passwd"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST['email']
        rollno = request.POST["rollno"]
        semester = request.POST["semester"]
        dept = request.POST["department"]

        if int(rollno) < 211001 or int(rollno) > 211999:
            messages.warning(request, "invalid Rollno")
            return redirect('signup')
        
        if int(semester) == 0:
            messages.warning(request, "Invalid semester")
            return redirect('signup')
        
        if dept == "NULL":
                messages.error(request,"Select valid Department")
                return redirect('signup')

        myuser = User.objects.create_user(username, email, passwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.email = email
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()


        if myuser is not None:
            login(request,myuser)
            studentData = Student.objects.create(username = request.user, rollno = rollno, semester = semester, department = dept)
            studentData.save()
        else:
            messages.danger(request, "Student model error.")

        messages.success(request, "Your Account has been created succesfully.")

        return redirect('signin')    
    return render(request, 'authentication/signup.html')