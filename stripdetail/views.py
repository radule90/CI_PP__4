from .models import StripDetail
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class StripDetailListView(ListView):
    '''
    Class based view that shows list of comic strips with details
    '''
    model = StripDetail
    template_name = 'stripdetail/strips.html'
    context_object_name = 'strips'
    paginate_by = 9
