from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import pooja
# Create your views here.

def func(request):
	if request.method =='POST':
		x=request.POST.get("nm")
		y=request.POST.get("add")
		z=request.POST.get("empID")
		a =pooja(name=x,address=y,empID=z)
		a.save()
		print(x,y,z)
	else:
			return render(request,"page1.html",context={})
	return HttpResponse("printed on Console, please Check!!")
			