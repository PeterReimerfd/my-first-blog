from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.utils import timezone
import json

# Create your views here.

def index(request):
    print("hello")
    return(HttpResponse('something'))

def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    print(posts.first().text)
    return render(request,'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post': post})

#def post_list(request):
 #   posts = Post.objects.all().order_by('published_date')
 #   print(posts)
 #   return render(request,'blog/post_list.html',{'posts': posts})