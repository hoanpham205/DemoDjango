from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def index(request):
    return HttpResponse("hello")
def add_post(request):
    a = PostForm()
    return render(request,'news/add_news.html',{'f':a})