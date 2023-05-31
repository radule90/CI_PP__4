from django.urls import path
from .views import (
    StripPostListView, StripPostCreateView, 
    StripPostDetailView, StripPostUpdateView)


urlpatterns = [
    path('', StripPostListView.as_view(), name='blog'),
    path('create/', StripPostCreateView.as_view(), name='create-post'),
    path('post/<slug:slug>/', StripPostDetailView.as_view(), name='post'),
    path('update/<slug:slug>/', 
    StripPostUpdateView.as_view(), name='update-post'),
]