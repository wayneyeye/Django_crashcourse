# -*- encoding: utf-8 -*-
from django import forms
from mysite import models
class PostForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=["mood",'nickname','message','del_pass']
    # def __init__(self,*args,**kwargs):
    #     super(PostForm,self).__init__(*args,**kwargs)
    #     self.fields['mood'].label='现在的心情'
    #     self.fields['nickname'].label='您的昵称'
    #     self.fields['message'].label='心情留言'
    #     self.fields['del_pass'].label='设置密码'
