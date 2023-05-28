from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import MemberSignUpForm
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
