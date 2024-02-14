from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login_link")
def home(request):
    return render(request,"home.html",{})


def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home_link")
        
        elif not user:
            err1 = "Not A User, Please Register"
            return render(request,"login_page.html",{"err":err1})
        
        else:
            return render(request,"login_page.html",{})
    else:
        return render(request,"login_page.html",{})


def logoutuser(request):
    logout(request)

    return redirect("login_link")

def reguser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email  = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]

        if User.objects.filter(username=username).exists():
            err1 ="Username already exists"

            return render(request,"register_page.html",{"err1":err1})
        
        elif User.objects.filter(email=email).exists():
            err2 ="Email already exists"

            return render(request,"register_page.html",{"err2":err2})
        
        else:
            createuser = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name = firstname,
                last_name = lastname
                
            )

            createuser.save()
            return redirect("login_link")
        
    else:
        return render(request,"register_page.html",{})

        
