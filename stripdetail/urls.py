from django.urls import path
from .views import (
    StripDetailListView, StripDetailCreateView, StripDetailUpdateView)

urlpatterns = [
    path('', StripDetailListView.as_view(), name='strip-list'),
    path('create/', StripDetailCreateView.as_view(), name='strip-create'),
    path('update/<slug:slug>/', StripDetailUpdateView.as_view(), 
         name='strip-update'),
]
