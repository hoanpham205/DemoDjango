from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm, SendEmail
from django.views import View

# Create your views here.

class IndexClass(View):
    def get(self,request):
        
        ketqua = '12323'
        return HttpResponse(ketqua)


class ClassSaveNew(View):
    def get(self,request):
        a = PostForm()
        return render(request,'news/add_news.html',{ 'f':a })
    
    def post(self,request):
        g = PostForm(request.POST)
        if  g.is_valid():
            g.save()
            return HttpResponse("Success")
        else :
            return HttpResponse("Error")
    
    
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
            
        