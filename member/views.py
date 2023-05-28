from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
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
    model = User
    form_class = MemberSignUpForm
    template_name = 'member/sign_up.html'
    success_url = reverse_lazy('home-page')


class MemberLoginView(LoginView):
    '''
    Class based view for member login
    '''
    template_name = 'member/sign_in.html'
    success_url = reverse_lazy('home-page')
