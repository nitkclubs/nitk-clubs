from django.db import models

# Create your models here.

class Event(models.Model):
    eventName = models.CharField(max_length=30)
    eventDescription = models.TextField()
    venue = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    eventImg = models.ImageField(upload_to="image/", default='')

    def __str__(self):
        return self.eventName