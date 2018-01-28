# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import get_template
from mysite import models
from django.http import HttpResponse
# Create your views here.
def index(request):
	template=get_template('index.html')
	try:
		urid=request.GET['user_id']
		urpass=request.GET['user_pass']
		b_year=request.GET['byear']
	except:
		urid=None	
	if urid!=None and urpass=='12345':
		verified=True
	else:
		verified=False
	years=range(1960,2021)
	colors=['Red','Green','Purple','White','Pink','Yellow']
	fcolor=request.GET.getlist('fcolor')
	html=template.render(locals())
	return HttpResponse(html)

def posts(request,pid=None,del_pass=None):
	template=get_template('posts.html')
	posts=models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
	moods=models.Mood.objects.all()
	try:
		urid=request.GET['user_id1']
		urpass=request.GET['user_pass']
		urpost=request.GET['user_post']
		urmood=request.GET['mood']
	except:
		urid=None
		message='Every field should be filled before submission!'

	if del_pass and pid:
		try:
			post=models.Post.objects.get(id=pid)
		except:
			post=None
		if post:
			if post.del_pass==del_pass:
				post.delete()
				message="Successfully Deleted!"
			else:
				message="Wrong password!"

	elif urid!=None:
		mood=models.Mood.objects.get(status=urmood)
		post=models.Post.objects.create(mood=mood,nickname=urid,del_pass=urpass,message=urpost)
		post.save()
		message="Sucessfully Saved! Please keep your password %s! The post will be published after censoring." %urpass
	
	html=template.render(locals())
	return HttpResponse(html)
