from django.shortcuts import render
from django.http import HttpResponse,Http404
from practice.models import Product
# Create your views here.
def about(request):
	html='''
<!doctype html>
<html lang="en">
<head>
  <title>The HTML5 Herald</title>
</head>
<body>
	<h1>Wayne Ye</h1>
	<hr>
	<p>Hi I am Wayne!</p>
</body>
</html>
'''
	return HttpResponse(html)

def listing(request):
	html='''
<!doctype html>
<html lang="en">
<head>
  <title>list of products</title>
</head>
<body>
	<h1>List of products</h1>
	<hr>
	<table width=400 border=1 bgcolor='#ccffcc'>
	{}
	</table>
</body>
</html>
'''
	products=Product.objects.all()
	tags="<tr><td>Product</td><td>sku</td><td>size</td></tr>"
	for p in products:
		tags=tags+"<tr><td>{}</td>".format(p.name)
		tags=tags+"<td>{}</td>".format(p.sku)
		tags=tags+"<td>{}</td></tr>".format(p.size)
	return HttpResponse(html.format(tags))

def disp_detail(request,sku):
	html='''
<!doctype html>
<html lang="en">
<head>
  <title>list of products</title>
</head>
<body>
	<h1>List of products</h1>
	<hr>
	<table width=400 border=1 bgcolor='#ccffcc'>
	{}
	</table>
</body>
</html>
'''
	try:
		products=Product.objects.filter(sku=sku)
	except Product.DoesNotExist:
		raise Http404('Unknown sku')
	if len(products)==0:
		raise Http404('Unknown sku')
	tags="<tr><td>Product</td><td>sku</td><td>size</td></tr>"
	for p in products:
		tags=tags+"<tr><td>{}</td>".format(p.name)
		tags=tags+"<td>{}</td>".format(p.sku)
		tags=tags+"<td>{}</td></tr>".format(p.size)
	return HttpResponse(html.format(tags))