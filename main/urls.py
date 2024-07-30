# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
]
