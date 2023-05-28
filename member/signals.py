from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member

# Signals to create instance of Member, when User is created
# Solution is taken and adapted from https://www.youtube.com/@coreyms


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.member.save()
