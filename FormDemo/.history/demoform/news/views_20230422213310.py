from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm, SendEmail
from django.views import View

# Create your views here.

def IndexClass(View):
    def get(self,request):
        ketqua = '12323'
    return HttpResponse(ketqua)

def add_post(request):
    a = PostForm()
    return render(request,'news/add_news.html',{ 'f':a })

def save_news(request):
    if request.method == 'POST':
        g = PostForm(request.POST)
        if  g.is_valid():
            g.save()
            return HttpResponse("Success")
        else :
            return HttpResponse("Error")
    else:
        return HttpResponse("Not POST Request")
    
def email_news(request):
    b = SendEmail()
    return render(request,'news/email.html',{ 'f':b})

def process(request): 
    if request.method == 'POST':
        m = SendEmail(request.POST)
        if m.is_valid():
            # tieude = m.cleaned_data["title"]
            # content = m.cleaned_data["content"]
            # cc = m.cleaned_data["cc"]
            # email = m.cleaned_data["email"]
            # context = { 'td':tieude, 'c':cc, 'b': content, 'd':email, }
            context2 = {'email_data': m}
            return render(request,'news/print_email.html', context2)
        
        else:
            return HttpResponse("form not validate")
    else:
        return HttpResponse("Error")        
            
        