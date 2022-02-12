from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# view 내에 선언된 함수로 인자로 HttpRequest라는 객체를 Django가 전달해준다.
def post_list(request):
    my_name = '장고웹프레임워크'
    http_method = request.method
    return HttpResponse('''
        <h2>Welcome {name}</h2>
        <p>Http Method : {method}<p/>
        <p>Http headers user-Agent : {header}</p>
        <p>Http Path : {mypath}</p>
    '''.format(name=my_name, method=http_method, header=request.headers['user_agent'], mypath=request.path))
