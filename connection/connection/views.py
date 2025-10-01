from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import product,order
from .forms import Formorder,FormProduct
def home(request):
    return render(request,'home.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('dashboard')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('userdashboard')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def Register_view(request):
    if request.method =='POST':
        First_Name = request.POST['Name']
        Email=request.POST['Email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['cnfm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'registration.html')
def user_dash(request):
    products=product.objects.all()
    orders=order.objects.all()
    return render(request,'user_dashboard.html',{'products':products,'orders':orders})
def change_status(request,pk):
    status=order.objects.get(id=pk)
    if request.method=="POST":
        form =Formorder(request.POST,instance=status)
        if form.is_valid:
            form.save()
            messages.success(request, '')
            return redirect('dashboard')
    else:
        form=Formorder(instance=status)
    return render(request, 'update.html',{'form':form,'status':status})
def make_order(request,pk):
    item=product.objects.get(id=pk)
    user=request.user
    data=order.objects.create(buyer=user,item=item)
    data.save()
    return redirect('dashboard')
def update_product(request,pk):
    pdt=product.objects.get(id=pk)
    if request.method=="POST":
        form =FormProduct(request.POST,instance=pdt)
        form.save()
        return redirect('dashboard')
    else:
        form=FormProduct(instance=pdt)
        return render(request,'update.html',{'form':form,'product':pdt})
    return render(request,'update.html',{'form':form,'product':pdt})
def add_product(request):
    if request.method=="POST" and request.FILES['product_image']:
        product_name=request.POST['product_name']
        image=request.FILES['product_image']
        category =request.POST['category']
        price=request.POST['price']
        data=product.objects.create(user=request.user,image=image,product_name=product_name,category=category,price=price)
        data.save()
        return redirect('dashboard')
    return render(request,'addproduct.html')