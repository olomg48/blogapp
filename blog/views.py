from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404



def home(request):
	posts = Post.objects.all()
	return render(request, 'blog/home.html',{'posts':posts})