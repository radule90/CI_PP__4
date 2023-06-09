from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce import models as tinymce_models


# Create your models here.


class Member(models.Model):
    '''
    Member class for member profile that extends django User model
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = tinymce_models.HTMLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = CloudinaryField('avatar')

    def __str__(self):
        return self.user.username
