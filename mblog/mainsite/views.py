from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template
from .models import Post
# Create your views here.
def homepage(request):
	template=get_template('index.html')
	now=datetime.now()
	posts=Post.objects.all()
	html=template.render(locals())
	return HttpResponse(html)
