from django.shortcuts import render,redirect
from django.http import HttpResponse
from fishmartapp. models import *
from . models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index3(request):
    data = martdb.objects.all()
    return render(request,'index3.html', {'data':data})


def contact(request):
    data = martdb.objects.all()
    return render(request,'contact.html',{'data':data})



def condata(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = contactdb(name=name,email=email,phone=phone,subject=subject,message=message)
        data.save()
    return redirect('index3')

    
def contable(request):
    data=contactdb.objects.all()
    return render(request,'contable.html',{'data':data})


def register(request):
    data = martdb.objects.all()
    return render(request,'register.html',{'data':data})


def regi(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phonenumber=request.POST.get('phonenumber')
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=registerdb(firstname=firstname,lastname=lastname,phonenumber=phonenumber,username=username,password=password)
        data.save()
    return redirect('index3')
    

def registration(request):
    data=registerdb.objects.all()
    return render(request,'registration.html',{'data':data})


def userlogin(request):
    data = martdb.objects.all()
    return render(request,'userlogin.html',{'data':data})

def userin(request):
    if request.method=="POST":
        username_a=request.POST.get('username')
        password_a=request.POST.get('password')
        print(password_a)
        print(username_a)
        if registerdb.objects.filter(username=username_a,password=password_a).exists():
            data=registerdb.objects.filter(username=username_a,password=password_a).values('firstname','lastname','phonenumber','id').first()
            request.session['firstname']=data['firstname']
            request.session['lastname']=data['lastname']
            request.session['phonenumber']=data['phonenumber']
            request.session['username']=username_a
            request.session['password']= password_a
            request.session['id']=data['id']
            return redirect('index3')
        else:
            return render(request,'userlogin.html',{'msg':"sorry... invalid username or password"})
    else:
        return redirect('userlogin')
   
def logout(request):
    del request.session['firstname']
    del request.session['lastname']
    del request.session['phonenumber']
    del request.session['username']
    del request.session['password']
    del request.session['id']
    return redirect('index3')

def products(request,cat):
    if(cat=="all"):
        data1=productdb.objects.all()
    else:
        data1 = productdb.objects.filter(category=cat)
    data = martdb.objects.all()
    return render(request,'products.html',{'data1':data1,'data':data})


def single(request,pid):
    data1 = productdb.objects.filter(id=pid)
    data = martdb.objects.all()
    return render(request,'single.html',{'data':data,'data1':data1})

def cart(request):
    data = martdb.objects.all()
    u  = request.session.get('id')
    data1 = cartdb.objects.filter(userid=u,status=0)
    total = cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'total':total,'data1':data1})


def check(request):
    data = martdb.objects.all()
    u  = request.session.get('id')
    data1 = cartdb.objects.filter(userid=u,status=0)
    total = cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request ,'check.html',{'data':data,'total':total,'data1':data1})

def cart1(request,pid):
    if request.method=="POST":
        userid=request.POST.get('userid')
        total=request.POST.get('total')
        quantity=request.POST.get('quantity')
        data=cartdb(productid=productdb.objects.get(id=pid),userid=registerdb.objects.get(id=userid),total=total,quantity=quantity,status=0)
        data.save()
    return redirect('cart')

def deletec(request,cid):
    data=cartdb.objects.filter(id=cid)
    data.delete()
    return redirect('cart')

def checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        u = request.session.get('id')
        order = cartdb.objects.filter(userid=u,status=0)
        for i in order:
            data = checkoutdb(cartid=cartdb.objects.get(id=i.id),name=name,email=email,mobile=mobile,address=address)
            data.save()
            cartdb.objects.filter(id=i.id).update(status=1)
    return redirect('index3')
 

@csrf_exempt

def cart_update(request):
    if request.method == "POST":
        cartid = request.POST.get('pid')
        q = request.POST.get('qty')
        print(q)
        p = request.POST.get('price')
        tot = float(q)*float(p)
        print(tot)
        data=cartdb.objects.filter(id=cartid).update(total=tot,quantity=q)
    return HttpResponse()

def orders(request):
    data=checkoutdb.objects.all()
    return render(request,'orders.html',{'data':data})


def getorder (request):
    if request.method=="POST":
        cartid = request.POST.get('cartid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        data = checkoutdb(cartid=cartid,name=name,email=email,mobile=mobile,address=address)
        data.save()
        return redirect(orders)