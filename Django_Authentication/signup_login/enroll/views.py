from django.shortcuts import render,HttpResponseRedirect
from .forms import Signup
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

#sign in 
def signup(request):
	if request.method == 'POST':
		fm = Signup(request.POST)
		if fm.is_valid():
			fm.save()
	else:
		fm = Signup()
	return render(request,'enroll/register.html',{'form':fm})


#log in
def user_log(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			fm = AuthenticationForm(request=request,data=request.POST)
			if fm.is_valid():
				uname = fm.cleaned_data['username']
				upass = fm.cleaned_data['password']
				user = authenticate(username=uname,password=upass)
				if user is not None:
					login(request, user)
					messages.add_message(request,messages.SUCCESS,"Log in Successfully !!!")
					return HttpResponseRedirect('/profile/')
		else:
			fm = AuthenticationForm()
		return render(request,'enroll/login.html',{"form":fm})
	else:
		return HttpResponseRedirect('/profile/')


def user_profile(request):
	if request.user.is_authenticated:
		return render(request,'enroll/profile.html',{'name':request.user})
	else:
		return HttpResponseRedirect('/login/')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')