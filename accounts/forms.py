from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=100, help_text='Required. Add a valid email address')
	country = forms.CharField(max_length=50)
	phno = forms.CharField(max_length=20)
	city = forms.CharField(max_length=50)
	class Meta:
		model = Account
		fields = ("email", "username","country", "city", "phno", "password1", "password2")