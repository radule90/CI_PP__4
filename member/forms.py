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


class MemberProfileForm(forms.ModelForm):
    about = forms.Textarea()
    location = forms.CharField()
    avatar = CloudinaryFileField(
        options={
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'avatars'
        }
    )

    class Meta:
        model = Member
        fields = ['location', 'avatar', 'about']
