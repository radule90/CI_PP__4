from django.urls import path
from .views import StripPostListView, StripPostCreateView


urlpatterns = [
    path('', StripPostListView.as_view(), name='blog'),
    path('create/', StripPostCreateView.as_view(), name='create-post')
]