from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=150)
    ingress = models.CharField(max_length=500)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='authored')
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='events', default='placeholder-event.png')
    participants = models.ManyToManyField(User, related_name='participating', blank=True)
    max_participants = models.IntegerField()
    signup_start = models.DateTimeField()
    signup_end = models.DateTimeField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()

    def signup_open(self):
        return self.signup_start < timezone.now() < self.signup_end

    def __str__(self):
        return '{}: {}'.format(self.timestamp.date(), self.title)


class EventComment(models.Model):
    event = models.ForeignKey(Event)
    author = models.ForeignKey(User)
    timestamp = models.DateTimeField(default=timezone.now)
    text = models.TextField()