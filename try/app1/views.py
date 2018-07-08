# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests,json
from requests_oauthlib import OAuth1
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import contactform,signupform,marksheetform,twitterform,currencyform,rssform,chatform
from .models import signup,marksheet,twitter,currency,rss,chat
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
		    print instance.userid
		    instance.save() 
		    context = {
		"title":"MARK ADDED"
		}

	return render(request,"add.html",context)
def marks(request):
	querry = marksheet.objects.all()
	for i in querry:
		print i.mark
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
def converter(request):
	form = currencyform(request.POST or None)
	title = ""
	context={
	"form":form,
	"title":title
	}
	if form.is_valid():
		instance =form.save(commit=False)

		if instance.fro and instance.to:
			api_key = "a9da6bd7112437cbe655914c40024b97"
			url = "http://data.fixer.io/api/latest?access_key="+api_key
			r = requests.get(url)
			d = r.json()
			c= d["rates"]
			base = "EUR"
			if instance.fro==base:
				result =  float(c[instance.to])*float(instance.amount)
			else:
				x = float(1/c[instance.fro])
				y =  float(x*float(instance.amount))
				result = y*c[instance.to]
			instance.save() 
			context = {
		"result":result,
		"title":"CONVEETED AMOUNT IS :"
		}

	return render(request,"converter.html",context)
def rsss(request):
	form = rssform(request.POST or None)
	title = ""
	context={
	"form":form,
	"title":title
	}
	if form.is_valid():
		instance =form.save(commit=False)
		if instance.url:
			urls = instance.url
			r = feedparser.parse(urls)
			a = []
			for i in r["entries"]:
				a.append("*******"+i["title"]+"*********"+"\n"+i["published"]+"\::-->"+i["summary"]+":"+i["link"])
			instance.save() 
			context = {
		"title":"MARK ADDED",
		"a":a
		}

	return render(request,"rsss.html",context)
def chat(request):
	form = chatform(request.POST or None)
	title = "ENTER THE MESSAGE HERE"
	context={
	"form":form,
	"title":title
	}
	if form.is_valid():
		instance =form.save(commit=False)
		if instance.msg:
			msgs = instance.msg
			url = "https://matrix.org/_matrix/client/r0/rooms/!FXclHICUyrLMhiVPYq:matrix.org/send/m.room.message?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDI4Y2lkIHVzZXJfaWQgPSBAYW1hbGRldmNzOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSBRU2MsYU9vMn5LWEw9MnQ3CjAwMmZzaWduYXR1cmUgnufaSzM_y5gwiYnRnuqt2OpTIPaywRDJjJ37rbGJ0zQK"
			content = {"msgtype":"m.text","body":msgs}
			data = json.dumps(content)
			r = requests.post(url,data=data)
			if r.status_code == 200:
				instance.save() 
				context = {
		"title":"Successfully sent!!!!",
		
		}

	return render(request,"chat.html",context)