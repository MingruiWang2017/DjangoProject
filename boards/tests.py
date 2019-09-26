from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home


# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')  # 根据‘home’反向解析出url
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)