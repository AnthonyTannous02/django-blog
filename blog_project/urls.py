from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("posts", views.view_posts, name="posts-page"),
    path("posts/<slug:slug>", views.load_one_post, name="load-post"),
]
