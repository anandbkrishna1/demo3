from django.contrib import messages, auth

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Watch,CartItem
from app.forms import*

# from app.form import*
# Create your views here.


def index(request):
    content=Watch.objects.all()
    d=User.objects.all()
    data={
        'result':content,
        'user1':d
        
    }
    return render(request,'index.html',data)

def details(request,id):
    product=Watch.objects.get(pk=id)
    print(product)
    data={
        'data':product
    }
    return render(request,'detail.html',data)


def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass')
        password2=request.POST.get('cpass')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists!!!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username=username,email=email,password=password1)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')
    return render(request,'signup.html')

def user_login (request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        print(username,password1)
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            messages.info(request,'user not exists')
            print('user no exist')
            return redirect(user_login)
    return render(request,'login.html')



def user_logout(request):
    logout(request)
    return redirect(index)

def all(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'all.html',data)
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    # total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, })
 
def add_to_cart(request, product_id):
    product = Watch.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(view_cart)
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect(view_cart)
 
 

# def home(request):
#     return render(request,'index.html')


