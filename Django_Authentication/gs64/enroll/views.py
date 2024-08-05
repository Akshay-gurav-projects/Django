from django.shortcuts import render
from .forms import Sign_user
from django.contrib import messages
# Create your views here.

def sign_up(request):
	if request.method == "POST":
		fm = Sign_user(request.POST)
		if fm.is_valid():
			fm.save()
			messages.SUCCESS(request,'Account created successfully')
		fm = Sign_user()
	else:
		fm = Sign_user()
	return render(request,'enroll/signup.html',{'form':fm})