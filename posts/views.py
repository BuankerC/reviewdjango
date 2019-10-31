from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'posts/index.html')

def detail(request, id):
    get_object_or_404(Post, id=id)

def create(request):
    pass