# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2019/9/30 15:49
@ desc: 
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve

from ..models import Topic, Board, Post
from ..views import topic_posts, PostListView


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Djange', description='Django board.')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        topic = Topic.objects.create(subject='Hello, world', board=board, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk': board.pk, 'topic_pk': topic.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/board/1/topics/1/')
        # self.assertEquals(view.func, topic_posts)
        self.assertEquals(view.func.view_class, PostListView)
