from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator


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

    def __str__(self):
        return self.subject


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
