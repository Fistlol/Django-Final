from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class BookJournalBase(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.id} : {self.name}'


class Book(BookJournalBase):
    num_pages = models.IntegerField(null=True)
    genre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.id} : {self.name}'


class Journal(BookJournalBase):
    type = models.CharField(max_length=200, null=True)
    publisher = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.id} : {self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created')


post_save.connect(create_profile, sender=User)


def updated_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()


post_save.connect(updated_profile, sender=User)