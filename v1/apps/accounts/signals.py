import uuid

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from . import models


@receiver(pre_save, sender=models.User)
def token_handler(sender, **kwargs):
    instance = kwargs["instance"]
    instance.token = str(uuid.uuid4()).replace('-', '')
