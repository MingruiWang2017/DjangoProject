# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2019/9/27 16:39
"""
from django.test import TestCase
from ..forms import SignUpForm

class SignUpFormTests(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)