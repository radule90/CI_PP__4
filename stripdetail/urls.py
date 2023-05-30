from django.urls import path
from .views import StripDetailListView, StripDetailCreateView

urlpatterns = [
    path('', StripDetailListView.as_view(), name='strip-list'),
    path('create/', StripDetailCreateView.as_view(), name='strip-create'),
]
