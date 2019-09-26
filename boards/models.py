from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)  # 限制名称唯一性
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)  # 创建对象时，设置为当前时间
    board = models.ForeignKey(Board, related_name='topics')  # 外键，related_name告诉关联的模型用什么字段引用本模型
    starter = models.ForeignKey(User, related_name='topics')

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')  # +表示不建立反向关系，即不关心用户修改过哪些帖子