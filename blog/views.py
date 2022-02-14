from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post

# 글상세정보
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Views 내에 선언된 함수로 인자로 HttpRequest 라는 객체를 Django가 전달해준다.
# 글목록
def post_list(request):
    my_name = '장고웹프레임워크'
    http_method = request.method

    # return HttpResponse('''
    #     <h2>Welcome {name}</h2>
    #     <p>Http Method : {method}</p>
    #     <p>Http headers User-Agent : {header}</p>
    #     <p>Http Path : {mypath}</p>
    # '''.format(name=my_name, method=http_method, header=request.headers['user-agent'], mypath=request.path))

    # return render(request, 'blog/post_list.html')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts})