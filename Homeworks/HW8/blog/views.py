from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Post 
from django.views.generic import TemplateView

# Create your views here.

# Create views for indext.html (home page)
def index(request):
    # Get the objects through Post and order them based on publication date
    list = Post.objects.order_by('-pub_date') 

    # call the index.html page
    return render(request, 'blog/index.html', {'list': list}) 

# Create views for every individual blog post
def post(request, blog_id):
    # Get the objects through Post based on a specefic id
    post = Post.objects.get(pk=blog_id)

    # call the post.html page
    return render(request, 'blog/post.html', {'post': post}) 
