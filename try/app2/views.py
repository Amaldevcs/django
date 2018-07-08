# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import requests,json
from requests_oauthlib import OAuth1
from django.contrib.auth.models import User
from django.shortcuts import render
from .form import contactform,signupform,companyform,applyform,appliedform
from .models import signup,company,apply,appliedd
import feedparser
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
	form = companyform(request.POST or None)
	title = ""
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
		    print instance.fullname
		    print instance.userid
		    instance.save() 
		    context = {
		"title":"OK !!!"
		}

	return render(request,"add.html",context)
def jobs(request):
	querry = company.objects.all()
	context={
	"querry":querry,
	}
	return render(request,"marksheet.html",context)

def deletes(request,pk):
	querry = company.objects.get(id=pk)
	querry1 = querry.userid
	try:
		if int(request.user.id) == int(querry1):
			company.objects.filter(id=pk).delete()
		context = {"title":"OOPS! ENTERY DELETED!! BUT YOU CAN DELETE ONLY YOUR COMPANY ENTRY###ANOTHERS NOT ALLOWED####"
		}

	    
		
	except:
		context={"title":"YOU CAN'T DELETE IT!!"
		}
	

	
	
	return render(request,"delete.html",context)
def appl(request):
	title = 'Apply Here##please enter the company ID to userid###'
	form = applyform(request.POST or None)
	#if request.user.is_authenticated():
		#title = "My title%s"%(request.user)
	context = {'title':title,
	'form':form,
	}
	if form.is_valid():
		instance =form.save(commit=False)
		if instance.fullname:
			instance.save()
			context = {
	'title':"Thank You"
	}
	return render(request,'apply.html',context)
def applicant(request):
	querry = apply.objects.filter(userid=request.user.id)
	print querry
	context={
	"querry":querry,
	}
	return render(request,"applicant.html",context)
def applied(request):
	title = 'TO SEE YOUR APPLIED>>>ENTER YOUR MAIL_ID'
	form = appliedform(request.POST or None)
	#if request.user.is_authenticated():
		#title = "My title%s"%(request.user)
	context = {'title':title,
	'form':form,
	}
	if form.is_valid():
		instance =form.save(commit=False)
		if instance.email:
			querry = apply.objects.filter(email=instance.email)
			print querry
			a=[]
			for i in querry:
				print i.userid
				querry1 = company.objects.filter(userid=i.userid)
				a.append(querry1)
				instance.save()
				print a
				context = {"querry":a,
	'title':"Thank You"
	}
	return render(request,'applied.html',context)