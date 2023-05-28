from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

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
    fields = ['username', 'first_name', 'last_name', 'email', ]
    template_name = 'member/sign_up.html'
    success_url = reverse_lazy('home-page')
