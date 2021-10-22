from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import dispatcher
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import Settings
from .signals import object_viewed_signal


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class PronuanceWords(models.Model):
    words_id = models.AutoField(primary_key=True)
    words = models.TextField(null=True)
    novel = models.TextField(null=True)
    count = models.IntegerField(blank=True, null=True)
    wordlength = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pronuance_words'
