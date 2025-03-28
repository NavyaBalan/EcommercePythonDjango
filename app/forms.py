from django import forms

# from app.models import Customer
from django.contrib.auth.forms import UserCreationForm ,UsernameField,AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User

from app.models import Customer

class LoginForm(AuthenticationForm):
    username=UsernameField(widget = forms.TextInput(attrs=
       {'autofocus' : 'True', 'class' : 'form-control'}))
    password= forms.CharField(widget = forms.PasswordInput(attrs=
       {'autocomplete' : 'current-password', 'class' : 'form-control'}))

class UserRegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'true',
        'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'}))

    password1 =forms.CharField(label='password',widget=forms.PasswordInput(attrs=
        {'class':'form-control'}))
    password2 =forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs=
        {'class':'form-control'}))

class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
  



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'name','locality','city','mobile','state','zip_code']
        widgets = {
            'name' : forms.TextInput( attrs={'class' : 'form-control'}),
            'locality' : forms.TextInput(attrs={'class' : 'form-control'}),
            'city' : forms.TextInput(attrs={'class' : 'form-control'}),
            'mobile' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'state' : forms.Select(attrs={'class' : 'form-control'}),
            'zip_code' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }

class UserPasswordChangeForm(PasswordChangeForm):
   
    oldpassword = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password', 'class': 'form-control'}))

 
    new_password1 = forms.CharField(label='New Password' , widget = forms.PasswordInput(attrs=
       {'autocomplete' : 'current-password', 'class' : 'form-control'}))
    
    new_password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput(attrs=
       {'autocomplete' : 'current-password', 'class' : 'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label = 'New Password',widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class' : 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput(attrs=
       {'autocomplete' : 'current-password', 'class' : 'form-control'}))





