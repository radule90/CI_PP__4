from django.contrib import admin
from .models import StripDetail

# Register your models here.


@admin.register(StripDetail)
class StripDetailAdmin(admin.ModelAdmin):
    '''
    Add StripDetail model to Admin panel
    '''
    pass
