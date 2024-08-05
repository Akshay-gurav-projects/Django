from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class SignInForm(UserCreationForm):
	password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		labels = {'username':'User Name',
				  'firstname':'First Name',
				  'lastname':'Last Name',
				  'email':'E-mail'}


class EditUserProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		labels = {'email':'E-mail'}