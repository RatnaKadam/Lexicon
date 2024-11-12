from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    my_dict = {'insert_me':"Hello from views!!"}
    return render(request, 'index.html', context=my_dict)

def blog_view(request):
    return render(request, 'blog.html')