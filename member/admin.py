from django.contrib import admin
from .models import Member

# Register your models here.


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    '''
    Add Member model to Admin panel
    '''
    list_display = ('user', 'location')
