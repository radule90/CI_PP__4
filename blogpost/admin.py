from django.contrib import admin
from .models import StripPost


# Register your models here.
@admin.register(StripPost)
class StripPostAdmin(admin.ModelAdmin):
    '''
    Add StripPost model to Admin panel
    '''
    list_display = ('title', 'author', 'created_on', 'approved')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'content']
    list_filter = ('approved', 'created_on')
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        queryset.update(approved=True)
