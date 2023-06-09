from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import ListView
from .forms import MemberSignUpForm, MemberUpdateForm, MemberProfileForm
from .models import Member
from blogpost.models import StripPost
from django.db.models import Q

# Create your views here.


def home(request):
    '''
    Function based view to render home page
    '''
    return render(request, 'index.html')


class SearchListView(ListView):
    '''
    Class based Search view thta filters StripPost objects based on
    user search query and render results on search html
    Idea for code is taken from:
    https://stackoverflow.com/questions/13416502/django-search-form-in-class-based-listview
    '''
    model = StripPost
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(
                Q(content__icontains=query) |
                Q(title__icontains=query) |
                Q(strip__title__icontains=query) |
                Q(strip__writer__icontains=query) |
                Q(strip__artist__icontains=query) |
                Q(strip__publisher__icontains=query))
        else:
            object_list = self.model.objects.none()
        return object_list


class MemberCreateView(SuccessMessageMixin, CreateView):
    '''
    Class based view for member registration
    '''
    model = Member
    form_class = MemberSignUpForm
    success_url = reverse_lazy('sign-in')
    success_message = 'You Have Successfully Signed Up!'


class MemberLoginView(SuccessMessageMixin, LoginView):
    '''
    Class based view for member login
    '''
    template_name = 'member/member_sign_in.html'
    success_url = reverse_lazy('home-page')
    success_message = 'You Have Successfully Signed In!'


class MemberLogoutView(LoginRequiredMixin, LogoutView):
    '''
    Class based view for member logout
    '''
    template_name = 'member/member_sign_out.html'
    login_url = 'home-page'


class MemberProfileDetailView(
     LoginRequiredMixin, DetailView, MultipleObjectMixin):
    '''
    Class based view for User profile details
    And shows member blog posts
    https://gist.github.com/nspo/5ab1ecde7e918a5fa266298ca5b15f08
    '''
    model = User
    template_name = 'member/member_profile.html'
    context_object_name = 'profile'
    login_url = 'sign-in'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        user = self.get_object()
        object_list = StripPost.objects.filter(author=user.id)
        context = super(MemberProfileDetailView, self).get_context_data(
            object_list=object_list, **kwargs)
        return context


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
    return render(request, 'member/member_profile_update.html', context)


class MemberProfileDeleteView(
        LoginRequiredMixin,
        UserPassesTestMixin,
        SuccessMessageMixin,
        DeleteView
):
    '''
    Class based view to delete User and member profile
    Customized get_success_url() so that success message show
    success url
    Test for authorization, check if request user is owner
    of the profile we want to delete
    Test is inspired by code found on:
    https://stackoverflow.com/questions/64978195/access-editing-profile-only-by-profile-owner-using-userpassestestmixin-showing-e
    '''
    model = User
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('home-page')
    success_message = 'Your Profile Has Been Successfully Deleted'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super().get_success_url()

    def test_func(self):
        return self.request.user == self.get_object()
