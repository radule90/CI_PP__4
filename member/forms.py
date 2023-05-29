from cloudinary.forms import CloudinaryFileField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member


class MemberSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class MemberUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']
        exclude = ['password1', 'password2']


class MemberProfileForm(forms.ModelForm):
    about = forms.Textarea()
    location = forms.CharField(required=False)
    avatar = CloudinaryFileField(
        options={
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'default_image': 'avatar/',
            'folder': 'avatars',
            'use_filename': True
        }
    )

    class Meta:
        model = Member
        fields = ['location', 'avatar', 'about']
