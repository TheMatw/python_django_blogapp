from django import forms
from .models import Post

# ModelForm을 상속받는 PostModelForm 클래스 정의
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)