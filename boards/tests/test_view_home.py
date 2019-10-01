# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2019/9/30 14:42
@ desc: 
"""
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve

from ..models import Board
from ..views import home, BoardListView

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')  # 根据‘home’反向解析出url
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        # self.assertEqual(view.func, home)
        self.assertEqual(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
