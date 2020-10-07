"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls'),name='home'),
    path('register/',user_views.register,name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('profile/', user_views.profile,name='profile'),
    path('post/',user_views.NewPost.as_view(),name = 'posting'),
    path('<int:post_id>/',user_views.detail, name = 'detail'),
    path('delete/<pk>/',user_views.PostDelete.as_view(template_name = 'users/delete.html'), name = 'delete'),
    path('update/<pk>/',user_views.PostUpdate.as_view(),name = 'update'),
]
