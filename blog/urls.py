from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
	path('',views.PostListView.as_view(),name='home'),

]