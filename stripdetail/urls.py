from django.urls import path
from .views import StripDetailListView

urlpatterns = [
    path('', StripDetailListView.as_view(), name='strip-list'),
]
