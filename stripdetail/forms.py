from django import forms
from .models import StripDetail
from datetime import datetime
from cloudinary.forms import CloudinaryFileField


def possible_years(first_year_in_scroll, last_year_in_scroll):
    '''
    Function that generates list of possible years
    in range based on two given arguments
    Code is taken from
    https://stackoverflow.com/questions/49051017/year-field-in-django
    '''
    p_year = []
    for i in range(first_year_in_scroll, last_year_in_scroll, -1):
        p_year_tuple = str(i), i
        p_year.append(p_year_tuple)
    return p_year


class StripDetailForm(forms.ModelForm):
    year = forms.ChoiceField(choices=possible_years(
        ((datetime.now()).year), 1900),)
    strip_cover = CloudinaryFileField(
        options={
            'crop': 'fit',
            'width': 700,
            'height': 933,
            'folder': 'covers',
            'use_filename': True
        }
    )

    class Meta:
        model = StripDetail
        fields = ['title', 'strip_cover', 'artist', 'writer',
                  'publisher', 'year', 'coloring', 'binding',
                  'country', 'pages']
