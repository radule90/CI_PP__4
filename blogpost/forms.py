from cloudinary.forms import CloudinaryFileField
from django import forms
from .models import StripPost


class StripPostForm(forms.ModelForm):
    featured_image = CloudinaryFileField(
        options={
            'crop': 'fit',
            'width': 1200,
            'height': 628,
            'folder': 'blog_images',
            'use_filename': True
        }
    )

    class Meta:
        model = StripPost
        fields = ['strip', 'title', 'content', 'featured_image']
