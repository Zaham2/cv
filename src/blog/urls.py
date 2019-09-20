from django.urls import path

from . import views

urlpatterns = [
    path('', views.allBlogs, name='allblogs'),
    path('zeft/<int:blog_id>/', views.oneBlog, name='oneblog')  # the tag part means the title has a number in it
    # The tag says: If the title has an int... I'll save it as blog_id... this blog_id is the passed to views.oneBlog
]
