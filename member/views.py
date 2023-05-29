from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import MemberSignUpForm, MemberProfileForm
from .models import Member

# Create your views here.


def home(request):
    '''
    Function based view to render home page
    '''
    return render(request, 'index.html')


class MemberCreateView(CreateView):
    '''
    Class based view for member registration
    '''
    model = Member
    form_class = MemberSignUpForm
    template_name = 'member/sign_up.html'
    success_url = reverse_lazy('home-page')


class MemberLoginView(LoginView):
    '''
    Class based view for member login
    '''
    template_name = 'member/sign_in.html'
    success_url = reverse_lazy('home-page')


class MemberLogoutView(LogoutView):
    '''
    Class based view for member logout
    '''
    template_name = 'member/sign_out.html'


class MemberProfileDetailView(DetailView):
    '''
    Class based view for User profile details
    '''
    model = User
    template_name = 'member/profile.html'
    context_object_name = 'profile'


def profile_update(request, pk):
    '''
    Code used for solution is originaly made Corey Schafer 
    https://www.youtube.com/@coreyms
    I have adjusted it for purpose of this project
    So that both forms User and Profile which extends User model can be updated
    '''
    if request.method == 'POST':
        user_form = MemberSignUpForm(request.POST, instance=request.user)
        profile_form = MemberProfileForm(
            request.POST, instance=request.user.member)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = MemberSignUpForm(instance=request.user)
        profile_form = MemberProfileForm(instance=request.user.member)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'member/profile_update.html', context)
