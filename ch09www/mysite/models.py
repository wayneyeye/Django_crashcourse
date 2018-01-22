# _*_ encoding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __unicode__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='不愿意透露身份的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    def __unicode__(self):
        return self.message
