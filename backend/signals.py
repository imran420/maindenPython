from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Article
from django.utils.text import slugify


@receiver(pre_save, sender=Article)
def add_slug(sender, instance, *arg, **Kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
