from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content',)
        widget ={
            'title': forms.TextField(attrs={'class': 'form-control'}),
            'content': forms.TextField(attrs={'class': 'form-content'}),
        }
        
class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'tieude'}))
    email= forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'phihoan', 'id' :'noidung'}))
    cc = forms.BooleanField(required=False)
    