from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member

from django.core.mail import send_mail
from django.conf import settings


# Signals to create instance of Member, when User is created
# Solution is taken and adapted from https://www.youtube.com/@coreyms


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user=instance
        member = Member.objects.create(user=user)

        send_mail(
            "Welcome to StripTeaser Blog",
            "We value your opinion and invite you to share your reviews.",
            settings.EMAIL_HOST_USER,
            [member.user.email],
            fail_silently=False,
        )

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.member.save()
