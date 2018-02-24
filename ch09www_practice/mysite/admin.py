# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=('nickname','message','enabled','pub_time')
	ordering=('-pub_time',)

class MoodAdmin(admin.ModelAdmin):
	list_display = ('status',)
	def status(self,instance):
		return instance.name
admin.site.register(models.Mood,MoodAdmin)
admin.site.register(models.Post,PostAdmin)