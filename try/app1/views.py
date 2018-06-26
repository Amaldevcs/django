# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests,json
from requests_oauthlib import OAuth1
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import contactform,signupform,marksheetform,twitterform
from .models import signup,marksheet,twitter
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
		    print instance.fullname
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
		if int(request.user.id) == int(querry1):
			marksheet.objects.filter(id=pk).delete()
		context = {"title":"OOPS! ENTERY DELETED!!"
		}

	    
		
	except:
		context={"title":"YOU CAN'T DELETE IT!!"
		}
	

	
	
	return render(request,"delete.html",context)

def tweets(request):
	form = twitterform(request.POST or None)
	title = "ENTER YOUR USER NAME "
	context={
	"form":form,
	"title":title
	}
	if form.is_valid():
		instance =form.save(commit=False)

		if instance.fullname:
			API_Key= "VBTj4JqebIFDctJlztF2xpd0P"
			API_Secret =  "pVlDfHthTeQhsqVqVRgNduwwQIPwXxE08LKBlzPqCq2SIAWo1J"
			Access_Token ="1010899301818658820-JpNNgTA5RMIiX7Ufe9fqUAcBgz1ora"
			Access_Token_Secret ="GHRf6rPmX4x0zpQ6YdLD6dboe1E71d9XHqRnJN60wRqIS"
			username = instance.fullname
			url=" https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&tweet_mode=extended&count=10"
			auth = OAuth1(API_Key,API_Secret,Access_Token,Access_Token_Secret)
			r = requests.get(url,auth=auth)
			d= r.json()
			a=[]
			#print r.status_code,d
			for i in d:
				if i["full_text"]:
					a.append(i["full_text"])
					
			instance.save()
			print a 
			context = {
		"title":"YOUR LAST TWEETS ARE :",
		"a":a

		}

	return render(request,"tweet.html",context)