from django import forms
from django.forms import TextInput, Textarea

from django.contrib import admin

from .models import MenuItem, MainInfo, Registration
from .models import Article
from .models import Schedule

# Definne specific Admin models here
class ArticleAdminForm( forms.ModelForm ):
	content1 = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))
	content2 = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))
	class Meta:
		fields = "__all__" 
		model = Article

class ArticleAdmin( admin.ModelAdmin ):
    form = ArticleAdminForm 
"""
class ScheduleAdminForm( forms.ModelForm ):
	content1 = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))
	content2 = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))
	content3 = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))
	class Meta:
		fields = "__all__" 
		model = Schedule

class ScheduleAdmin( admin.ModelAdmin ):
    form = ScheduleAdminForm 
"""
	
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(MainInfo)
admin.site.register(Article, ArticleAdmin)
#admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Schedule)
admin.site.register(Registration)

