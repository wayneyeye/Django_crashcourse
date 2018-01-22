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
