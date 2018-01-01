from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template
from .models import Post #That's the new syntax for explicit relative imports. It means import from the current package.
# Create your views here.
def homepage(request):
	template=get_template('index.html')
	now=datetime.now()
	posts=Post.objects.all()
	html=template.render(locals())
	return HttpResponse(html)


def showpost(request,slug):
	template=get_template('post.html')
	try:
		post=Post.objects.get(slug=slug) ##fetch the post corresponds to the slug
		now=datetime.now()
		if post !=None:	
			html=template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')
