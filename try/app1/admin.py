#coding: utf-8 -*5-
from __future__ import unicode_literals
from django.contrib import admin
from .forms import signupform
# Register your models here.
from .models import signup
class signupadmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp","update"]
	form = signupform
	#class Meta:
	#	model=signup

admin.site.register(signup,signupadmin)