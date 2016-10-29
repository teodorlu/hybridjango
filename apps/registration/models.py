import os
from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def get_graduation_year(grade):
    return (timezone.now() + timedelta(weeks=-26)).year + int(grade)


def five_years():
    return timezone.now().year + 5


def user_folder(instance, filename):
    return os.path.join('users', instance.user.username, filename)


class Hybrid(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=50, blank=True)
    member = models.BooleanField(default=False)
    graduation_year = models.IntegerField(default=five_years)
    image = models.ImageField(upload_to=user_folder, default='placeholder-profile.jpg')
    gender = models.CharField(max_length=1, blank=True)
    specialization = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=150, blank=True, default='Hybrid')

    def get_full_name(self):
        if self.middle_name:
            first_name = self.user.first_name + ' ' + self.middle_name
        else:
            first_name = self.user.first_name
        return first_name + ' ' + self.user.last_name

    def get_grade(self):
        return self.graduation_year - (timezone.now() - timedelta(weeks=26)).year

    def __str__(self):
        return self.user.username