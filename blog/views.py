from django.http import HttpResponse
from posts.models import Post, Vote
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


    