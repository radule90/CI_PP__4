from .models import StripDetail
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    paginate_by = 6


class StripDetailCreateView(
        LoginRequiredMixin, SuccessMessageMixin, CreateView):
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
    success_message = 'Strip Successfully Added!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StripDetailUpdateView(
        LoginRequiredMixin, UserPassesTestMixin, 
        SuccessMessageMixin, UpdateView):
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
    success_message = 'Strip Successfully Updated!'

    def test_func(self):
        return self.request.user == self.get_object().user


class StripDetailDeleteView(
        LoginRequiredMixin, UserPassesTestMixin, 
        SuccessMessageMixin, DeleteView):
    '''
    Class based view that delete comic strip
    Tests if request user is object creator
    '''
    model = StripDetail
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('strip-list')
    login_url = 'sign-in'
    success_message = 'Strip Successfully Deleted!'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super().get_success_url()

    def test_func(self):
        return self.request.user == self.get_object().user
