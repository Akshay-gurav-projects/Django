from django.shortcuts import render,HttpResponseRedirect
from .forms import SignInForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def user_signin(request):
	if request.method == 'POST':
		fm=SignInForm(request.POST)
		if fm.is_valid():
			fm.save()
			messages.success(request,"Account created !!!")
	else:
		fm = SignInForm()
	return render(request,'enroll/sign_up.html',{'form':fm})


def user_login(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			fm = AuthenticationForm(request=request,data=request.POST)
			if fm.is_valid():
				uname = fm.cleaned_data['username']
				upass = fm.cleaned_data['password']
				user = authenticate(username=uname,password=upass)
				if user is not None:
					login(request,user)
					messages.success(request,"Log in successfully!!")
					return HttpResponseRedirect('/profile/')
		else:
			fm=AuthenticationForm()
		return render(request,'enroll/log_in.html',{'form':fm})
	else:
		return HttpResponseRedirect('/profile/')
		

#user profile
def user_profile(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			if request.user.is_superuser == True:
				fm = EditAdminProfileForm(request.POST,instance=request.user)
				users = User.objects.all()
			else:
				fm = EditUserProfileForm(request.POST,instance=request.user)
				users = None
			if fm.is_valid():
				messages.success(request,"Profile Updated !!")
				fm.save()
		else:
			if request.user.is_superuser == True:
				fm=EditAdminProfileForm(instance=request.user)
				users = User.objects.all()
			else:
				fm = EditUserProfileForm(instance=request.user)
				users = None
		return render(request,'enroll/profile.html',{'name':request.user,'form':fm, 'users':users})
	else:
		return HttpResponseRedirect('/login/')
	


	
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

#change password with old password
def change_pass(request):
	if request.user.is_authenticated:
		fm=PasswordChangeForm(user=request.user,data=request.POST)
		if fm.is_valid():
			fm.save()
			update_session_auth_hash(request,fm.user)
			messages.success(request,"Password change successfully!!")
			return HttpResponseRedirect('/profile/')
		else:
			fm=PasswordChangeForm(user=request.user)
		return render(request,'enroll/changepass.html',{'form':fm})
	else:
		return HttpResponseRedirect('/login/')


def user_detail(request,id):
	if request.user.is_authenticated:
		pi = User.objects.get(pk=id)
		fm = EditAdminProfileForm(instance=pi)
		return render(request,'enroll/userdetail.html',{'form':fm})
	else:
		return HttpResponseRedirect('/login/')