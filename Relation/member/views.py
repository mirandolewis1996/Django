from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from member.models import Member
# Create your views here.

def home(request):

    if request.method == "POST":
        x = request.POST["firstname"]
        y = request.POST["lastname"]

        z = Member()

        z.firstname = x
        z.lastname  = y

        if True:
            z.save()
            messages.success(request,"Successfully Created")
            return redirect("home_link")
        
      
    
    else:
        return render(request,"member/home.html",{})

def listview(request):

    listmem = Member.objects.all()
    paginator = Paginator(listmem, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,"member/listview.html",{"page_obj":page_obj})   

def delpage(request,pk):
    
    dellis = Member.objects.get(pk=pk)

    return render(request,"member/dellist.html",{"dellis":dellis})

def delmember(request,pk):

    delmem = Member.objects.get(pk=pk)

    delmem.delete()

    return redirect("list_link")

def editmember(request,pk):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]

        edimem = Member.objects.get(pk=pk)

        edimem.firstname = firstname
        edimem.lastname= lastname

        edimem.save()
        return redirect("list_link")
    
    else:
        edimem = Member.objects.get(pk=pk)

        return render(request,"member/editlist.html",{"firstname":edimem.firstname,"lastname":edimem.lastname})
