"""ch08www_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import index
from mysite.views import posts
from mysite.views import listing
from mysite.views import posting
from mysite.views import post2db
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    # url(r'^(\d+)/(\w+)/$', posts), #redirect to delete
    # url(r'^posts$', posts),
    url(r'^posting$', posting),
    url(r'^listing$', listing),
    url(r'^post2db$', post2db),
]
