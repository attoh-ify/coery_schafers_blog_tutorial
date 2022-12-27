from django.shortcuts import render

posts = (
    {
        'author': 'Attoh-Alexander',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': '25th december 2022'
    },
    {
        'author': 'Attoh-Tobe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': '27th december 2022'
    },
    {
        'author': 'Attoh-Chico',
        'title': 'Blog post 3',
        'content': 'third post content',
        'date_posted': '30th december 2022'
    }
)

# Create your views here.


def home(request):
    # django database
    context = {'posts': posts}

    # render html template
    return render(request, 'blogapp/home.html', context)


def about(request):
    return render(request, 'blogapp/about.html', {'title': 'About'})
