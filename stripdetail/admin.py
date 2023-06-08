from django.contrib import admin
from .models import StripDetail

# Register your models here.


@admin.register(StripDetail)
class StripDetailAdmin(admin.ModelAdmin):
    '''
    Add StripDetail model to Admin panel
    '''
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'artist', 'writer', 'publisher')
    search_fields = ['title', 'artist', 'writer', 'publisher']
    list_filter = ('artist', 'writer', 'publisher')
