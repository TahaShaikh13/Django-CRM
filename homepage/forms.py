from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Data


class RegistrationForm (UserCreationForm):
    first_name = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    username = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
class Meta:
    model = User
    fields = ('username','first_name','last_name','email','password1','password2')

class Add_data_form (forms.ModelForm):
    first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First_name","class":"form-control"}),label="")
    last_name  = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last_name","class":"form-control"}),label="")
    email = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}),label="")
    phone_no = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Phone_no","class":"form-control"}),label="")
    address =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}),label="")
    city = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"City","class":"form-control"}),label="")
    state =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"State","class":"form-control"}),label="")
    pincode = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode","class":"form-control"}),label="")

    class Meta:
        model = Data
        exclude = ("user",)
