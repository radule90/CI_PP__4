from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

from .forms import MemberSignUpForm, MemberUpdateForm, MemberProfileForm
from .models import Member

# Create your views here.


def home(request):
    '''
    Function based view to render home page
    '''
    return render(request, 'index.html')


class MemberCreateView(SuccessMessageMixin, CreateView):
    '''
    Class based view for member registration
    '''
    model = Member
    form_class = MemberSignUpForm
    template_name = 'member/sign_up.html'
    success_url = reverse_lazy('sign-in')
    success_message = 'You Have Successfully Signed Up!'


class MemberLoginView(SuccessMessageMixin, LoginView):
    '''
    Class based view for member login
    '''
    template_name = 'member/sign_in.html'
    success_url = reverse_lazy('home-page')
    success_message = 'You Have Successfully Signed In!'


class MemberLogoutView(LoginRequiredMixin, LogoutView):
    '''
    Class based view for member logout
    '''
    template_name = 'member/sign_out.html'
    login_url = 'sign-in'


class MemberProfileDetailView(LoginRequiredMixin, DetailView):
    '''
    Class based view for User profile details
    '''
    model = User
    template_name = 'member/profile.html'
    context_object_name = 'profile'
    login_url = 'sign-in'


@login_required(login_url="sign-in")
def profile_update(request, pk):
    '''
    Code used for solution is originaly made Corey Schafer 
    https://www.youtube.com/@coreyms
    I have adjusted it for purpose of this project
    So that both forms User and Profile which extends User model can be updated
    '''
    if request.method == 'POST':
        user_form = MemberUpdateForm(request.POST, instance=request.user)
        profile_form = MemberProfileForm(
            request.POST, request.FILES, instance=request.user.member)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile Was Successfully Updated!')
            return redirect('profile', pk=request.user.id)
    else:
        user_form = MemberUpdateForm(instance=request.user)
        profile_form = MemberProfileForm(instance=request.user.member)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'member/profile_update.html', context)


class MemberProfileDeleteView(
        LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    '''
    Class based view to delete User and member profile
    Customized get_success_url() so that success message show
    success url
    '''
    model = User
    template_name = 'member/profile_delete.html'
    success_url = reverse_lazy('home-page')
    success_message = 'Your Profile Has Been Successfully Deleted'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super().get_success_url()
