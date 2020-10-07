from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


def detail(request, post_id):
	post = Post.objects.get(pk = post_id)
	return render(request,'users/detail.html',{'post':post})

	
class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model  = Post
	success_url = reverse_lazy('home')
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostUpdate( LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title','content']
	template_name = 'blog/update.html'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class NewPost(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']
	template_name = 'users/posting.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
