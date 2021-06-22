from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


def hello(request):
    if request.method == "GET":
        print("get 请求")
        name = request.GET.get("name","")
    return render(request,"hello.html",{"n":name})


def index(request):
    return render(request,"index.html")