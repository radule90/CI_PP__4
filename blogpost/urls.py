from django.urls import path
from .views import StripPostListView, StripPostCreateView, StripPostDetailView


urlpatterns = [
    path('', StripPostListView.as_view(), name='blog'),
    path('create/', StripPostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>', StripPostDetailView.as_view(), name='post'),
]