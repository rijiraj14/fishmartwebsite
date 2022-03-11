from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from martapp.models import cartdb, checkoutdb, contactdb, registerdb

def index(request):
     ucount=martdb.objects.all().count()
     ucount1=productdb.objects.all().count()
     ucount2=registerdb.objects.all().count()
     ucount3=contactdb.objects.all().count()
     ucount4=checkoutdb.objects.all().count()
     return render(request,'index.html',{'ucount':ucount,'ucount1':ucount1,'ucount2':ucount2,'ucount3':ucount3,'ucount4':ucount4})

def addcategory(request):
    return render(request,'addcategory.html')

def viewcategory(request):
    data=martdb.objects.all()
    return render(request,'viewcategory.html',{'data':data})


def getdata (request):
    if request.method=='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image=request.FILES['image'] 
        data = martdb(name=name,description=description,photo=image)
        data.save()
        return redirect(viewcategory)



def edit(request,martid):
        data=martdb.objects.filter(id=martid)
        return render(request,'edit.html',{'data':data})


def update(request,martid):
    if request.method=='POST':
        name=request.POST.get('name')
        des=request.POST.get('description')
        try:
            image=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=martdb.objects.get(id=martid).photo
        martdb.objects.filter(id=martid).update(name=name,description=des,photo=file,)
        return redirect('viewcategory')


def delete(request,martid):
    data=martdb.objects.filter(id=martid).delete()
    return redirect('viewcategory')


def addproduct(request):
    data=martdb.objects.all()
    return render(request,'addproduct.html',{'data':data})

def viewproduct(request):
    data=productdb.objects.all()
    return render(request,'viewproduct.html',{'data':data})


def getdata1 (request):
    if request.method=='POST':
        name = request.POST.get('productname')
        weight = request.POST.get('weight')
        price = request.POST.get('price')
        image=request.FILES['image'] 
        data = productdb(productname=name,weight=weight,price=price,photo=image)
        data.save()
        return redirect(viewproduct)



def edit1(request,productid):
        data=productdb.objects.filter(id=productid)
        return render(request,'edit1.html',{'data':data})


def update1(request,productid):
    if request.method=='POST':
        name=request.POST.get('productname')
        weight=request.POST.get('weight')
        price=request.POST.get('price')
        try:
            image=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=productid).photo
        productdb.objects.filter(id=productid).update(productname=name,weight=weight,price=price,photo=file)
        return redirect('viewproduct')


def delete1(request,productid):
    data=productdb.objects.filter(id=productid).delete()
    return redirect('viewproduct')

def adminlogin(request):
    return render(request,'login.html')


def adlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user = authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('index')
        else:
            return render(request,'login.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return redirect('adminlogin')

