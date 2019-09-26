from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board

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

    #模板引擎渲染视图
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})