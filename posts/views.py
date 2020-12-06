from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):
    # return HttpResponse("Hello world! このページは当行のインデックスです")
    posts = Post.objects.order_by("-published")
    return render(request, "posts/index.html", {"posts":posts})

def home(request):
    return render(request,"posts/home.html")

def post_detail(request, post_id):
    post = get_object_or_404( Post,pk=post_id)
    return render(request, "posts/post_detail.html", {"post":post})

def product(request):
    return render(request, "posts/product.html")

def about(request):
    return render(request, "posts/about.html")
# Create your views here.