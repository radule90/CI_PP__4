from django.urls import path
from . import views
from .views import MemberCreateView, MemberLoginView


urlpatterns = [
    path('', views.home, name='home-page'),
    path('member/sign_up/', MemberCreateView.as_view(), name='sign-up'),
    path('member/sign_in/', MemberLoginView.as_view(), name='sign-in'),
]
