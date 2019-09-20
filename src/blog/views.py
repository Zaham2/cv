from django.shortcuts import render, get_object_or_404
from .models import Blog


def allBlogs(request):
    blogs = Blog.objects
    return render(request, 'allblogs.html', {'allblogs': blogs})


def oneBlog(request, blog_id):
    oneblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'oneblog.html', {'oneblog': oneblog})
