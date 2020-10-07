from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 2

class PostDetailView(DetailView):
	model = Post
	