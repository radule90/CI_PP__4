from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


# Create your models here.


class StripDetail(models.Model):
    '''
    For this model, most of the data is mandatory because it is 
    about the technical details of the comic, in the future it will be expanded 
    (for example, genre, language, author of the cover)
    '''
    COLORING_CHOICE = (('Color', 'Color'),
                       ('Black and White', 'Black and White'),
                       ('Duotone', 'Duotone'))
    COVER_CHOICE = (('Hardcover', 'Hardcover'), ('Softcover',
                    'Softcover'), ('Trade Paperback', 'Trade Paperback'),
                    ('Floppy', 'Floppy'), ('Digital', 'Digital'))

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='details')
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=250, blank=False,
                            null=False, unique=True)
    strip_cover = CloudinaryField('cover')
    artist = models.CharField(max_length=100, blank=False, null=False)
    writer = models.CharField(max_length=100, blank=False, null=False)
    publisher = models.CharField(
        max_length=100, blank=False, null=False)
    year = models.PositiveIntegerField(blank=False, null=False)
    coloring = models.CharField(max_length=50, choices=COLORING_CHOICE)
    binding = models.CharField(
        max_length=50, null=False, blank=False, choices=COVER_CHOICE)
    country = CountryField(blank=False, null=False)
    pages = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        '''
        Auto populate slug field solution found on:
        https://learndjango.com/tutorials/django-slug-tutorial
        '''
        self.slug = slugify(self.title)
        super(StripDetail, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} | {self.publisher}'
