from django.shortcuts import render,redirect,get_list_or_404
from medstore.models import Medicine,Disease
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="login_link")
def med_home(request):

    if request.method == "POST":
        searchmed = request.POST["medsearch"]
        
        med = Medicine.objects.filter(medic_name__contains=searchmed)

        return render(request,"medstore/med_search.html",{"medic":med,"searchmed":searchmed})
       
    else:
        
        return render(request,"medstore/med_home.html",{})
   
        

    
    
    
@login_required(login_url="login_link")
def med_create(request):
    if request.user.is_staff:
        if request.method == "POST":
          med_name = request.POST["medname"]
          disease_id = request.POST.getlist("dislist")
          med_price = request.POST["medprice"]
          med_choice = request.POST.get("medcho")

          if med_name == "":
            err1 = "Enter Medicine Name"
            medcre = Disease.objects.all()
            return render(request,"medstore/med_create.html",{"err1":err1,"dis1":medcre}) 
       
          else:
            medcre = Medicine.objects.create(medic_name = med_name,medic_price = med_price,medic_choice = med_choice)
            medcre.disease.set(Disease.objects.filter(id__in=disease_id))
            return redirect("medlis_link")  
        else:
            medcre = Disease.objects.all()
            return render(request,"medstore/med_create.html",{"dis1":medcre})
    else:
        return redirect("home_link")   
    
  
@login_required(login_url="login_link")   
def medlist(request):
    
    med = Medicine.objects.all()

    return render(request,"medstore/med_list.html",{"med":med})

@login_required(login_url="login_link")
def medet(request,pk):

    medetail = Medicine.objects.get(pk=pk)


    return render(request,"medstore/med_detail.html",{"med":medetail})

@login_required(login_url="login_link")
def editmed(request,pk):

    if request.user.is_staff:
        mededit = Medicine.objects.get(pk=pk)
        dislist = Disease.objects.all()

        if request.method == "POST":
          mededit.medic_name = request.POST["medname"]
          mededit.medic_price = request.POST["medprice"]
          mededit.medic_choice = request.POST["medcho"]
          mededit.disease.set(request.POST.getlist("dislist"))

          mededit.save()

          return redirect("medlis_link")
    
        else:
          return render(request,"medstore/med_edit.html",{"med":mededit,"dis":dislist})
    else:
       return redirect("home_link")

def delpage(request,pk):
    if request.user.is_staff:
        delmed = Medicine.objects.get(pk=pk)

        return render(request,"medstore/med_del.html",{"delmed":delmed})
    else:
       return redirect("home_link")

@login_required(login_url="login_link")    
def delmed(request,pk):
    if request.user.is_staff:
       meddel = Medicine.objects.get(pk=pk)

       meddel.delete()

       return redirect("medlis_link")
    
    else:
        return redirect("home_link") 
    
def userlogin(request):
   if request.user.is_authenticated:
      return redirect("home_link")

   elif request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)

        if not user:
            err = "Not A User"
            return render(request,"medstore/login.html",{"err":err})
           
        elif user is not None:
            login(request,user)
            return redirect("home_link")
           
        else:
            return render(request,"medstore/login.html",{})
   else:
        return render(request,"medstore/login.html",{})       



def userlogout(request):
    
    logout(request)

    return redirect("login_link")


def userreg(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname  = request.POST["firstname"]
        lastname  = request.POST["lastname"]

        if User.objects.filter(username=username).exists():
            err = "username alredy exists"
            return render(request,"medstore/register.html",{"err":err})
        
        elif User.objects.filter(email=email).exists():
            err = "email alredy exists"
            return render(request,"medstore/register.html",{"err":err})
        

        else:
            usercre  = User.objects.create_user(
                first_name = firstname,
                last_name = lastname,
                username=username,
                password=password,
                email=email
            )

            usercre.save()
            return redirect("login_link")
        
    else:
        return render(request,"medstore/register.html",{})   

    
