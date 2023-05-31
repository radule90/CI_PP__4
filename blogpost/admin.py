from django.contrib import admin
from .models import StripPost


# Register your models here.
@admin.register(StripPost)
class StripPostAdmin(admin.ModelAdmin):
    '''
    Add StripPost model to Admin panel
    '''
    list_display = ('approved', 'title', 'author', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'content']
    list_filter = ('approved', 'created_on')