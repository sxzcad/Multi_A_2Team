from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    path=request.path
    resultstr=''
    if path =='/home':
        resultstr='<h1>여기는 home 입니다.</h1>'
    else:
        resultstr= '<h1>여기는 main 입니다.</h1>'
    return HttpResponse(resultstr)