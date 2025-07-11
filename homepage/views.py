from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegistrationForm,Add_data_form
from .models import Data

def homepage (request):

    data = Data.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged In")
            return redirect('homepage')
        else:
            messages.success(request,"Something wrong, Please try again")
            return redirect('homepage')
    else:
        return render (request, 'homepage.html', {'data':data})

def lo (requset):
    logout(requset)
    messages.success(requset,"You are logged Out")
    return redirect('homepage')

def register (request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password,)
            login(request,user)
            messages.success(request,"Successfully Registered !!")
            return redirect('homepage')
    else:
        form = RegistrationForm()
        return render (request, 'register.html', {'form':form})
    
    return render (request, 'register.html', {'form':form})

def customer_data (request,pk):
    if request.user.is_authenticated :
        customer_data = Data.objects.get(id=pk)
        return render (request,'data.html',{'customer_data':customer_data})
    else:
        messages.success(request,"You are not logged in, You have to be logged in to view data")
        return redirect('homepage')
    
def delete_data (request,pk):
    if request.user.is_authenticated:
        delete_data = Data.objects.get(id=pk)
        delete_data.delete()
        messages.success(request,"Data deleted Successfully")
        return redirect ('homepage')
    else:
        messages.success(request,"You are not logged in, You have to be logged in to view data")
        return redirect('homepage')
    
def add_data (request):
    form = Add_data_form(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_data = form.save()
                messages.success(request,"Data added Successfully")
                return redirect('homepage')
        return render (request,'add_data.html',{'form':form})
    else:
        messages.success(request,"You are not logged in, You have to be logged in to add data")
        return redirect('homepage')

def update_data (request,pk):
    if request.user.is_authenticated :
        current_data = Data.objects.get(id=pk)
        form = Add_data_form(request.POST or None,instance=current_data)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Updated Successfully")
            return redirect ('homepage')
        return render (request,'update_data.html',{'form':form})
    else:
        messages.success(request,"You are not logged in, You have to be logged in to add data")
        return redirect('homepage')
