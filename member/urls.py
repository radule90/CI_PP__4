from django.urls import path
from . import views
from .views import MemberCreateView


urlpatterns = [
    path('', views.home, name='home-page'),
    path('member/sign_up/', MemberCreateView.as_view(), name='sign-up'),
]
