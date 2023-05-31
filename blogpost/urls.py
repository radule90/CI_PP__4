from django.urls import path
from .views import StripPostListView


urlpatterns = [
    path('', StripPostListView.as_view(), name='blog')
]
