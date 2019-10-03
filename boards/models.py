from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from markdown import markdown
from django.utils.html import mark_safe
import math


# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)  # 限制名称唯一性
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_topics_count(self):
        return self.topics.count()

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)  # 创建对象时，设置为当前时间
    board = models.ForeignKey(Board, related_name='topics')  # 外键，related_name告诉关联的模型用什么字段引用本模型
    starter = models.ForeignKey(User, related_name='topics')
    views = models.PositiveIntegerField(default=0)  # 添加当前主题的访问次数

    def __str__(self):
        return self.subject

    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)

    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')  # +表示不建立反向关系，即不关心用户修改过哪些帖子

    def __str__(self):
        truncated_message = Truncator(self.message)  # Truncator ⼯具类，可以将⼀个⻓字符串截取为任意⻓度字符
        return truncated_message.chars(30)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))
