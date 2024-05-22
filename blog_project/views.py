from django.shortcuts import render
from datetime import date
from datetime import datetime
from django.http import Http404
from . import dummy_data

posts = dummy_data.posts
# Create your views here.


def index(request):
    sorted_posts = sorted(posts, key=lambda x: x["date"], reverse=True)
    latest_posts = sorted_posts[:3]
    return render(
        request,
        "blog_project/index.html",
        {
            "posts": latest_posts,
        },
    )


def view_posts(request):
    sorted_posts = sorted(posts, key=lambda x: x["date"], reverse=True)
    return render(
        request,
        "blog_project/posts.html",
        {
            "posts": sorted_posts,
        },
    )


def load_one_post(request, slug):
    try:
        post = next(post for post in posts if post['slug'] == slug)
        return render(
            request,
            "blog_project/post-detail.html",
            {
                "post": post,
            },
        )
    except:
        raise Http404()
