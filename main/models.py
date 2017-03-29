from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.

class MenuItem(models.Model):
    menuItem = models.CharField(max_length=50)
    linkTo = models.CharField("linkTo - Default: menuItem", max_length=50, blank=True, null=True)
    menuItemDescription = models.CharField(max_length=50)
    menuItemMouseOver = models.CharField(max_length=150, null=True, blank=True)
    order = models.IntegerField(default=1)
    active = models.IntegerField(default=1)
    loggedOnly = models.IntegerField(default=0)

    def __unicode__(self):
    	return str(self.order)+" "+self.menuItem+" - "+str(self.active)

class MainInfo(models.Model):
    title = models.CharField(max_length=200)
    tagLine = models.CharField(max_length=200)
    bgImage = models.ImageField(upload_to='static/main/siteImages', null=True)

    def __unicode__(self):
    	return self.title
 
class Article(models.Model):
    title = models.CharField(max_length=200)
    keyCode = models.CharField(max_length=40)
    tagLine = models.CharField(max_length=200)
    image = models.ImageField(upload_to='main/articleImages', blank=True)
    lid1 = models.CharField(max_length=100, blank=True)
    lid2 = models.CharField(max_length=100, blank=True)
    #content1 = models.CharField(max_length=800)
    content1 = models.TextField(blank=True)
    #content2 = models.CharField(max_length=800)
    content2 = models.TextField(blank=True, null=True)
    title3 = models.CharField(max_length=200, blank=True)
    content3 = models.TextField(blank=True)
    active = models.IntegerField(default=1)
    order = models.IntegerField(default=1)
    itemWidth = models.IntegerField("itemWidth - (12, 6, 3)",default=3, null=True)
    loggedOnly = models.IntegerField(default=0)

    def __unicode__(self):
        return self.keyCode +  " - " + self.title
 
class Schedule(models.Model):
    title = models.CharField(max_length=200)
    keyCode = models.CharField(max_length=40)
    
    image = models.ImageField(upload_to='static/main/scheduleImages', blank=True)
    dia_l1 = models.CharField(max_length=100, blank=True)
    dia_l2 = models.CharField(max_length=100, blank=True)
    tagLine = models.CharField(max_length=200)
    #content1 = models.CharField(max_length=800)
    content1 = models.TextField(blank=True)
    #content2 = models.CharField(max_length=800)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)

    order = models.IntegerField(default=1)
    active = models.IntegerField(default=1)
    loggedOnly = models.IntegerField(default=0)

    def __unicode__(self):
    	return self.keyCode +  " - " + self.title
 
class Registration(models.Model):
    name = models.CharField(max_length=30) 
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    cell = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    nif = models.CharField(max_length=16)

    f2fname = models.CharField(max_length=30, blank=True)
    f2email = models.CharField(max_length=40, blank=True)
    f2cell = models.CharField(max_length=30, blank=True)
    f2phone = models.CharField(max_length=30, blank=True)
    f2address = models.CharField(max_length=50, blank=True)
    f2city = models.CharField(max_length=50, blank=True)
    f2zip = models.CharField(max_length=50, blank=True)
    f2country = models.CharField(max_length=50, blank=True)
    f2nif = models.CharField(max_length=50, blank=True)

    modalidade = models.CharField(max_length=200, blank=True)
    modPag = models.CharField(max_length=30, blank=True)
    remarks = models.TextField(blank=True, null=True)

    regDate = models.DateTimeField("Reg Date: ", auto_now_add = True, blank=True, null=True)

    def __unicode__(self):
        return str(self.id) + " - "+self.name+" "+self.lname+" "+self.email+" "+self.f2fname+" "+str(self.regDate)
