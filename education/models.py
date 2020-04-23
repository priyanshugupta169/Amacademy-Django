from django.db import models
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os
# Create your models here.

class book(models.Model):
    filename = models.CharField(max_length=100,unique=True)
    filesize = models.IntegerField(default= 10)
    uploadstatus = models.CharField(max_length=30,default='success')
    uploadpath = models.FileField(upload_to='uploads/',unique=True)
    course = models.CharField(max_length=50,default='12')
    subject = models.CharField(max_length=50,default='science')



# class admin_register(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(primary_key=True)
#     password = models.CharField(max_length=100)
#     country = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     phno = models.CharField(max_length=20)

class contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    doubt = models.TextField()
    date = models.DateField(default=date.today)

