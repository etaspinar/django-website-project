from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

data = {
    "blogs": [
        {
            "id":1,
            "title": "JavaScript Dersleri",
            "image": "js.png",
            "is_active": True,
            "is_home": True,
            "description":"Kendinizi geliştirmek için bir numaralı kursumuz :D "
        },
        {
            "id":2,
            "title": "Komple Web Geliştirme Kursu",
            "image": "images.png",
            "is_active": True,
            "is_home": True,
            "description":"Kendinizi geliştirmek için bir numaralı kursumuz :D "
        },
        {
            "id":3,
            "title": "Django Web Geliştirme Kursu",
            "image": "django.png",
            "is_active": True,
            "is_home": True,
            "description":"En iyi Django Kursumuz "
        },
        {
            "id":4,
            "title": "Python Geliştirme Kursu",
            "image": "indir.png",
            "is_active": True,
            "is_home": False,
            "description":"Python öğrenin lan "
        },
    ]
}

def index(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request, "blog/index.html" , context)

def blogs(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request,"blog/blog.html", context)

def blogdetails(request , slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blogdetails.html",{
        "blog":blog
    })
