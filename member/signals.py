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
        user = instance
        member = Member.objects.create(user=user)

        message = f'''
        Dear {member.user.first_name},


        Welcome to StripTeaser Blog!
        We are delighted to have you as a new member of our community.

        At StripTeaser, we are dedicated to creating a space for comic book
        enthusiasts like you to share your passion, discover new stories,
        and connect with fellow fans. We believe that your unique perspective
        and insights will contribute to the vibrant discussions
        and engaging content within our blog.

        Feel free to explore our articles, dive into captivating comic book
        discussions, and stay updated with the latest news and releases.

        We're excited to have you on board and can't wait to see
        the valuable contributions you'll bring to our community.


        Best regards,
        StripTeaser Blog Team
        '''

        send_mail(
            "Welcome to StripTeaser Blog!",
            message,
            settings.EMAIL_HOST_USER,
            [member.user.email],
            fail_silently=False,
        )


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.member.save()
