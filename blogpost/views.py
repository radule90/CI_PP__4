from django.shortcuts import render
from .models import StripPost
from django.views.generic import ListView

# Create your views here.


class StripPostListView(ListView):
    '''
    Class based view that shows list of blog posts
    '''
    model = StripPost
    template_name = 'blogpost/blog.html'
    context_object_name = 'posts'
    paginate_by = 4
    