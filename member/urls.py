from django.urls import path
from . import views
from .views import (
    SearchListView,
    MemberCreateView,
    MemberLoginView,
    MemberLogoutView,
    MemberProfileDetailView,
    MemberProfileDeleteView
)


urlpatterns = [
    path('', views.home, name='home-page'),
    path('search/', SearchListView.as_view(), name='search'),
    path('member/sign_up/', MemberCreateView.as_view(), name='sign-up'),
    path('member/sign_in/', MemberLoginView.as_view(), name='sign-in'),
    path('member/sign_out/', MemberLogoutView.as_view(), name='sign-out'),
    path('member/profile/<int:pk>/',
         MemberProfileDetailView.as_view(), name='profile'),
    path('member/profile/update/<int:pk>/',
         views.profile_update, name='profile-update'),
    path('member/profile/delete/<int:pk>/',
         MemberProfileDeleteView.as_view(), name='profile-delete')
]
