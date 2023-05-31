from django.db import models
from django.contrib.auth.models import User
from stripdetail.models import StripDetail
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.


class StripPost(models.Model):
    '''
    Class for strip review posts
    '''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='spost')
    strip = models.ForeignKey(
        StripDetail, on_delete=models.CASCADE, related_name='strip')
    title = models.CharField(
        max_length=100, blank=False, null=False, unique=True)
    slug = models.SlugField(
        max_length=150, blank=False, null=False, unique=True)
    content = models.TextField(blank=False, null=False)
    featured_image = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        '''
        Auto populate slug field solution found on:
        https://learndjango.com/tutorials/django-slug-tutorial
        '''
        self.slug = slugify(self.title)
        super(StripPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title