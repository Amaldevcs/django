# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import contactform,signupform,marksheetform
from .models import signup,marksheet
# Create your views here.
def play(request):
	title = 'SignUp'
	form = signupform(request.POST or None)
	#if request.user.is_authenticated():
		#title = "My title%s"%(request.user)
	context = {'title':title,
	'form':form,
	}
	if form.is_valid():
		instance =form.save(commit=False)
		if not instance.fullname:
			instance.fullname="sali"
	        instance.save()
	        context = {
	'title':"Thank You"
	}
	if request.user.is_authenticated() and request.user.is_staff:
		context={
		"querry":'welcome back admin'
		}
	return render(request,'app1/play.html',context)
def contact(request):
	title = "CONTACT US"
	form = contactform(request.POST or None)
	context={"title":title,
	"form":form,
	}
	return render(request,"form.html",context)
def about(request):
	return render(request,"about.html",{})
def add(request):
	form = marksheetform(request.POST or None)
	title = "ADD MARK"
	context={
	"form":form,
	"title":title
	}
	if form.is_valid():
		instance =form.save(commit=False)
		form.cleaned_data["userid"]=request.user.id
		instance.userid=request.user.id

		if instance.fullname:
		    instance.userid=request.user.id
		    instance.save() 
		    context = {
		"title":"MARK ADDED"
		}

	return render(request,"add.html",context)
def marks(request):
	querry = marksheet.objects.all()
	context={
	"querry":querry,
	}
	return render(request,"marksheet.html",context)
def deletes(request,pk):
	querry = marksheet.objects.get(id=pk)
	querry1 = querry.userid
	try:
		int(request.user.id) == int(querry1)
		marksheet.objects.filter(id=pk).delete()
		context = {"title":"OOPS! ENTERY DELETED!!"
		}
	except:
		context={"title":"YOU CAN'T DELETE IT!!"
		}
	

	
	
	return render(request,"delete.html",context)
