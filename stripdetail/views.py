from .models import StripDetail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import StripDetailForm


# Create your views here.
class StripDetailListView(ListView):
    '''
    Class based view that shows list of comic strips with details
    '''
    model = StripDetail
    template_name = 'stripdetail/strips.html'
    context_object_name = 'strips'
    paginate_by = 3


class StripDetailCreateView(LoginRequiredMixin, CreateView):
    '''
    Class based view that for creating comic strips details
    form_valid override and set user of instance to current user
    Check if user is authenticated
    '''
    model = StripDetail
    form_class = StripDetailForm
    template_name = 'stripdetail/strip_create.html'
    success_url = reverse_lazy('strip-list')
    login_url = 'sign-in'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StripDetailUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    Class based view that for updating comic strips details
    Check if user is authenticated
    Tests if request user is object creator
    '''
    model = StripDetail
    form_class = StripDetailForm
    template_name = 'stripdetail/strip_update.html'
    success_url = reverse_lazy('strip-list')
    login_url = 'sign-in'

    def test_func(self):
        return self.request.user == self.get_object().user