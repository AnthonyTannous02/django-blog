from django.shortcuts import render, get_object_or_404
from datetime import date
from datetime import datetime
from django.http import Http404
from .models import Post, Author, Tag

# Create your views here.


def index(request):
    filtered_posts = Post.objects.all().order_by("-date")[:3]
    return render(
        request,
        "blog_project/index.html",
        {
            "posts": filtered_posts,
        },
    )


def view_posts(request):
    sorted_posts = Post.objects.all().order_by("-date")
    return render(
        request,
        "blog_project/posts.html",
        {
            "posts": sorted_posts,
        },
    )


def load_one_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog_project/post-detail.html",
        {
            "post": post,
            "post_tags": post.tags.all()
        },
    )
