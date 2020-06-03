from django.shortcuts import render, redirect
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
	posts = Post.objects.filter(author = request.user.id)
	return render(request, 'users/profile.html', {'posts':posts})


def posting(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = PostForm()
	return render(request,'users/posting.html',{'form':form})


def detail(request, post_id):
	post = Post.objects.get(pk = post_id)
	return render(request,'users/detail.html',{'post':post})