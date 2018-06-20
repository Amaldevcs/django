from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class signup(models.Model):
	email = models.EmailField()
	fullname = models.CharField(max_length=120,blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	update =models.DateTimeField(auto_now_add=False,auto_now=True)
	def __unicode__(self):
		return self.email
class marksheet(models.Model):
	fullname = models.CharField(max_length=120)
	mark = models.CharField(max_length=120)
	userid = models.CharField(max_length=120)
	def __unicode__(self):
		return self.fullname
