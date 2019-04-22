from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>welcome to my blog</h1>')

#render takes two three arguments
#1.request object
#2.path of the html.

""" To access variables from the templates
the django uses jinja engine to process the html pages"""

list_posts = [
    {"author":"kumara",
    "title":"blog post one",
    "content":"first post content",
    "date":"march 20,2019"},
    {"author":"Vicky",
    "title":"blog post two",
    "content":"Second post content",
    "date":"march 21,2019"}
]

def home(request):
    content = {
                'list_posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', content)

# def about(request):
#     return HttpResponse('<h1>This is about page</h1>')

def about(request):
    return render(request, 'blog/about.html')
