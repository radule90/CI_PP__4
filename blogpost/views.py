from django.shortcuts import render
from .models import StripPost
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import StripPostForm

# Create your views here.


class StripPostListView(ListView):
    '''
    Class based view that shows list of blog posts
    And queries approved posts
    '''
    model = StripPost
    queryset = StripPost.objects.filter(approved=True)
    context_object_name = 'posts'
    paginate_by = 4


class StripPostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    '''
    Class based view that for creating blog posts
    form_valid override and set author of instance to current user
    Check if user is authenticated
    '''
    model = StripPost
    form_class = StripPostForm
    success_url = reverse_lazy('blog')
    login_url = 'sign-in'
    success_message = 'Post Successfully Created!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StripPostDetailView(DetailView):
    '''
    Class based view for StripPost details
    '''
    model = StripPost
    context_object_name = 'post'


class StripPostUpdateView(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, UpdateView):
    '''
    Class based view that for updating blog posts
    Check if user is authenticated
    Tests if request user is object author
    '''
    model = StripPost
    form_class = StripPostForm
    template_name = 'blogpost/strippost_update.html'
    success_url = reverse_lazy('blog')
    login_url = 'sign-in'
    success_message = 'Post Successfully Updated!'

    def test_func(self):
        return self.request.user == self.get_object().author


class StripPostDeleteView(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, DeleteView):
    '''
    Class based view that delete blog post
    Tests if request user is object creator
    '''
    model = StripPost
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('blog')
    login_url = 'sign-in'
    success_message = 'Post Successfully Deleted!'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super().get_success_url()

    def test_func(self):
        return self.request.user == self.get_object().author
