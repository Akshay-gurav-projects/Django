from django.shortcuts import render,HttpResponseRedirect
from .forms import SignInForm,EditUserProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
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
		


def user_profile(request):
	if request.user.is_authenticated:
		fm = EditUserProfileForm(instance=request.user)
		return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
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
		