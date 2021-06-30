from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Staff


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='staff')
        instance.groups.add(group)

        Staff.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )


post_save.connect(customer_profile, sender=User)
