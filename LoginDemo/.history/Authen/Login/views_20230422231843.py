from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth.models import User
# Create your views here.


class IndexClass(View):
    def get(self,request):
        return HttpResponse("Chao comemmay")
    

class LoginClass(View):
    def get(self,request):
        return render(request, template_name='Login/login.html')
    def post(self,request):
        return HttpResponse("Login Success")