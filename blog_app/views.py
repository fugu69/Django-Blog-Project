from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# dummy data for demonstration
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 15, 2025',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 16, 2025',
    },
]

# creates response to the user
# (*app urls* -> function -> response)
def home(request):

    # allow access to the data content 
    context = {
        'posts': posts,
    }

    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog_app/home.html', context)

def about(request):
    # return HttpResponse('<h1>About page</h1>')
    return render(request, 'blog_app/about.html')
