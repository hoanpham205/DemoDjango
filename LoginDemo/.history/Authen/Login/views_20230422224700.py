from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.


class IndexClass(View):
    def get(self,request):
        return HttpResponse("Chao comemmay")
    

class LoginClass(View):
    def get(self,request):
        pass