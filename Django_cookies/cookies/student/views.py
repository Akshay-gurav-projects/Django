from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.

def setcookies(request):
	response = render(request,'student/set_cookies.html')
	response.set_cookie('name','rahul',expires=datetime.utcnow()+timedelta(days=2))
	return response

def getcookies(request):
	# name = request.COOKIES['name']
	name = request.COOKIES.get('name')
	return render(request,'student/get_cookies.html',{'name':name})

def delcookies(request):
	response = render(request,'student/del_cookies.html')
	response.delete_cookie('name')
	return response

