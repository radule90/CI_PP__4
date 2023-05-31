from django.shortcuts import render
from .models import StripPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView,
from .forms import StripPostForm

# Create your views here.


class StripPostListView(ListView):
    '''
    Class based view that shows list of blog posts
    '''
    model = StripPost
    template_name = 'blogpost/blog.html'
    context_object_name = 'posts'
    paginate_by = 4


class StripPostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    '''
    Class based view that for creating blog posts
    form_valid override and set author of instance to current user
    Check if user is authenticated
    '''
    model = StripDetail
    form_class = StripDetailForm
    template_name = 'blogpost/post_create.html'
    success_url = reverse_lazy('blog')
    login_url = 'sign-in'
    success_message = 'Post Successfully Created!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)