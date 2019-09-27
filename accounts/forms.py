# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2019/9/27 16:06
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):  # 继承UserCreationForm类
    email = forms.CharField(max_length=154, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

