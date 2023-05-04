from django.db import models

# Create your models here.
class Club(models.Model):
    clubId = models.AutoField(primary_key=True)
    clubName = models.CharField(max_length=30)
    clubDescription = models.TextField(null=True)
    clubHead = models.PositiveIntegerField(null=True)
    