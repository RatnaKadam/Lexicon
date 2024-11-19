from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me' : "Hello I am from app_folder/index.html !!!"}
    return render(request, 'app_folder/index.html',context = my_dict)