from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()  # Fetch all blog posts
    return render(request, 'index.html', {'posts': posts})

def base_template(request):
    return render(request,'base.html')


def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Fetch blog post by id
    return render(request, 'blog_detail.html', {'post': post})