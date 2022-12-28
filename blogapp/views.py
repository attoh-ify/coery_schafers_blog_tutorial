from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):
    # django database
    context = {'posts': Post.objects.all()}

    # render html template
    return render(request, 'blogapp/home.html', context)


def about(request):
    # django database

    # render html template
    return render(request, 'blogapp/about.html', {'title': 'About'})
