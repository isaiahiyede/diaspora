
from django import forms
from general.models import UserAccount
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from general.modelchoices import STATES, COUNTRY, TITLE
#from captcha.fields import CaptchaField
# from nocaptcha_recaptcha.fields import NoReCaptchaField
# from general.modelfield_choices import HOW_DID_YOU_FIND_US, INDUSTRY, PAYMENT

attrs3 = {'class': 'form-control','required': 'true'}



class LoginForm(forms.ModelForm):
    email      =    forms.EmailField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'form-group form-control'}))
    password   =    forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-group form-control'}))

    class Meta:
       # Associate form with a model
       	model = User
        fields = ('email','password',)



class UserForm(forms.ModelForm):
	first_name      =    forms.CharField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'class': 'form-group form-control','required': 'true'}))
	username        =    forms.CharField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'class': 'form-group form-control','required': 'true'}))
	email           =    forms.EmailField(max_length = 128, help_text = "",widget=forms.EmailInput(attrs={'class': 'form-group form-control','required': 'true'}))
	password        =    forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-group form-control','required': 'true'}))
	
	class Meta:
		model = User
		fields =  ('username','email','password','first_name',)



class UserAccountForm(forms.ModelForm):
    password2       = forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-group form-control','required': 'true'}))
    phone_number    = forms.CharField(max_length = 150, help_text="", widget=forms.TextInput(attrs=attrs3))
 
    
    class Meta:
        model = UserAccount
        fields = ('phone_number','password2',)