from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Club(models.Model):
    clubId = models.AutoField(primary_key=True)
    clubName = models.CharField(max_length=30)
    clubDescription = models.TextField(null=True)
    clubHead = models.ForeignKey(User,on_delete=models.CASCADE)
    clubImg = models.ImageField(null=True)
    