from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index,),
    path("blogs", views.blogs, name="blogs"),
    path("blog/<slug:slug>", views.blogdetails, name="blog_details")
]