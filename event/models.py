from django.db import models

# Create your models here.

class Event(models.Model):
    eventId = models.PositiveIntegerField()
    eventName = models.CharField(max_length=30)
    eventDescription = models.TextField()
    venue = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    duration = models.DurationField()