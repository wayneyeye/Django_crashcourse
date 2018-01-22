#_*_ encoding: utf-8 *_*
from django import forms
from mysite import models
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = ['height', 'male', 'website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['height'].label = '身高(cm)'
        self.fields['male'].label = '是男生吗'
        self.fields['website'].label = '个人网站'


class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

class DateInput(forms.DateInput):
    input_type = 'date'

class DiaryForm(forms.ModelForm):

    class Meta:
        model = models.Diary
        fields = ['budget', 'weight', 'note', 'ddate']
        widgets = {
            'ddate': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = '今日花费(元)'
        self.fields['weight'].label = '今日体重(KG)'
        self.fields['note'].label = '心情留言'
        self.fields['ddate'].label = '日期'
 