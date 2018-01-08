from django.shortcuts import render
from django.http import HttpResponse,Http404
from practice.models import Product
import random
from django.template.loader import get_template
# Create your views here.
def about(request):
	template=get_template('about.html')
	html=template.render()
	return HttpResponse(html)

def listing(request):
	template=get_template('disp.html')
	products=Product.objects.all()
	html=template.render({'products':products,'title':"We sell"})
	return HttpResponse(html)

def disp_detail(request,sku):
	try:
		products=Product.objects.filter(sku=sku)
	except Product.DoesNotExist:
		raise Http404('Unknown sku')
	if len(products)==0:
		raise Http404('Unknown sku')
	template=get_template('disp.html')
	html=template.render({'products':products,'title':"For sku = %s" %sku})
	return HttpResponse(html)

def index(request):
	template=get_template('index.html')
	lnum=random.randint(1,100)
	html=template.render({'lnum':lnum})
	return HttpResponse(html)