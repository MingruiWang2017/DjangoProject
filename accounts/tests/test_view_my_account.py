# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2019/10/2 14:30
@ desc: 
"""
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from ..views import UserUpdateView


class UnauthorizedTests(TestCase):
    def setUp(self):
        self.url = reverse('my_account')
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, f'{login_url}?next={self.url}')


class LoginMyAccountViewTests(TestCase):
    def setUp(self):
        username = 'john'
        password = '123456a?'
        User.objects.create_user(username=username, email='john@doe.com', password=password)
        url = reverse('my_account')
        self.client.login(username=username, password=password)
        self.response = self.client.get(url, kwargs={''})

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_func(self):
        view = resolve('/settings/account/')
        self.assertEquals(view.func.view_class, UserUpdateView)

    def test_contain_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
