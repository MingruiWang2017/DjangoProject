from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User

from .models import Board, Topic, Post
from .forms import NewTopicForm


# Create your views here.


def home(request):
    # 模板引擎渲染视图
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: 临时使用一个账号作为登录用户

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():  # 验证数据是否有效
            topic = form.save(commit=False)  # form与Topic相关联，save()方法返回保存的Topic实例
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: 重定向到创建出的Topic页面
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})
