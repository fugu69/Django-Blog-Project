from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post

# creates response to the user
# (*app urls* -> function -> response)
def home(request):

    # allow access to the data content 
    context = {
        # 'posts': posts,
        'posts': Post.objects.all()
    }

    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog_app/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog_app/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


def about(request):
    # return HttpResponse('<h1>About page</h1>')
    return render(request, 'blog_app/about.html', {'title': 'About'})
