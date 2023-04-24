from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("hello")
def add_post(request):
    return HttpResponse("Them bai viet")