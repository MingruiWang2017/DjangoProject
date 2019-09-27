# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2019/9/27 8:53
"""
from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'what is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the test is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
