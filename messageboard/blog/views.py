from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Patrick Davis',
        'title': 'One',
        'content': 'Lorem Ipsum.',
        'date_posted': "22 Sep 19"
    },
    {   'author': 'Patrick Davis',
        'title': 'Two',
        'content': 'Lorem Ipsum Two.',
        'date_posted': "21 Sep 19"
    },
]

def home(request):
    context= {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context={
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)