from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User

from .models import Board, Topic, Post
from .forms import NewTopicForm

# Create your views here.


def home(request):
    # return HttpResponse('Hello World!')

    # 简单页面
    # boards = Board.objects.all()
    # boards_names = list()
    #
    # for board in boards:
    #     boards_names.append(board.name)
    #
    # response_html = '<br>'.join(boards_names)
    #
    # return HttpResponse(response_html)

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

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: 临时使用一个账号作为登录用户

        topic = Topic.objects.create(  # 创建新的Topic
            subject = subject,
            board = board,
            starter = user
        )
        post = Post.objects.create(
            message = message,
            topic = topic,
            created_by = user
        )
        return redirect('board_topics', pk=board.pk)  # TODO: 重定向到创建出的Topic页面

    return render(request, 'new_topic.html', {'board':board})
