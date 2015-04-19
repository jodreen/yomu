from django.http import HttpResponse
from django.shortcuts import render
# from yomu.templates import *

def home(request):
    content = {
    'title' : 'My First Post',
    'author' : 'Giles',
    'date' : '18th September 2011',
    'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam cursus tempus dui, ut vulputate nisl eleifend eget. Aenean justo felis, dapibus quis vulputate at, porta et dolor. Praesent enim libero, malesuada nec vestibulum vitae, fermentum nec ligula. Etiam eget convallis turpis. Donec non sem justo.',
    }
    return render(request, 'index.html', content)

def mybooks(request):
    content = {
    'title' : 'My First Post',
    'author' : 'Giles',
    'date' : '18th September 2011',
    'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam cursus tempus dui, ut vulputate nisl eleifend eget. Aenean justo felis, dapibus quis vulputate at, porta et dolor. Praesent enim libero, malesuada nec vestibulum vitae, fermentum nec ligula. Etiam eget convallis turpis. Donec non sem justo.',
    }
    return render(request, 'index.html', content)

def profile(request):
    content = {
    'title' : 'My First Post',
    'author' : 'Giles',
    'date' : '18th September 2011',
    'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam cursus tempus dui, ut vulputate nisl eleifend eget. Aenean justo felis, dapibus quis vulputate at, porta et dolor. Praesent enim libero, malesuada nec vestibulum vitae, fermentum nec ligula. Etiam eget convallis turpis. Donec non sem justo.',
    }
    return render(request, 'index.html', content)
