from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegistrationForm,Add_data_form,AttendenceForm
from .models import Data,Department,Designation,Attendence
from django.db.models import Q

from django.utils import timezone


def homepage (request):
    query = request.GET.get('q')
    department_id = request.GET.get('department')
    designation_id = request.GET.get('designation')

    data = Data.objects.all()
    departments = Department.objects.all()
    designations = Designation.objects.all()

    if query:
        data = data.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(email__icontains = query) | Q(department__dep_name__icontains = query) | Q(designation__des_name__icontains = query))

    if department_id:
        data = data.filter(department_id=department_id)

    if designation_id:
        data = data.filter(designation_id=designation_id)

    context = {'data':data,
               'departments':departments,
               'designations':designations
               }

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
        return render (request, 'homepage.html', context)

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
    
def mark_attendence (request):
    if request.method == 'POST':
        form = AttendenceForm(request.POST)
        if form.is_valid():
            attendence = form.save(commit=False)
            attendence.timestamp = timezone.now()
            attendence.save()
            messages.success(request,"Attendence Marked Successfully")
            return redirect ('homepage')
    else:
        form = AttendenceForm
        return render (request,'mark_attendence.html',{'form':form})
    
def view_attendence (request):
    if request.user.is_authenticated :
        query = request.GET.get('q')
        date = request.GET.get('date')
        view_attendence = Attendence.objects.all().order_by('-date')
        if query:
            view_attendence = view_attendence.filter(Q(employee__first_name__icontains = query)| Q(employee__last_name__icontains = query))
        if date:
            view_attendence = view_attendence.filter(date=date)
        context = {'view_attendence':view_attendence,
                    'query':query,
                    'date':date,
                    }
        return render (request,'view_attendence.html',context)
    else:
        messages.success(request,"You are not Logged In, You have to be Logged In to view Attendence")
        return redirect ('homepage')
        