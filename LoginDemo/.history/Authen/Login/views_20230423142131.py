from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth import User, authenticate, login
# Create your views here.


class IndexClass(View):
    def get(self,request):
        return HttpResponse("Chao comemmay")
    

class LoginClass(View):
    def get(self,request):
        return render(request, 'Login/login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username="username", password="password")
        if my_user is not None:
            return HttpResponse("ERROR")
        
        login(request,my_user)
        return render(request, 'Login/LoginSuccess.html')