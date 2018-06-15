# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import contactform,signupform
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