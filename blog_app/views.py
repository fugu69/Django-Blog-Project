from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# creates response to the user
# (*app urls* -> function -> response)
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>About page</h1>')