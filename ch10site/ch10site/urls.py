"""ch09site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/(\w+)/$', views.index),
    url(r'^userinfo/$', views.userinfo),
    url(r'^post/$', views.posting),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    #url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('allauth.urls')),

]
