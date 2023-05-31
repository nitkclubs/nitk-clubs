from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Club(models.Model):
    clubId = models.AutoField(primary_key=True)
    clubName = models.CharField(max_length=30)
    clubDescription = models.TextField(null=True)
    clubHead = models.ForeignKey(User,on_delete=models.CASCADE)
    clubImg = models.ImageField(upload_to='clubImage/',null=True)
    
    def __str__(self):
        return self.clubName
    
class Members(models.Model):
    clubName = models.CharField(max_length=30)
    clubMember = models.ForeignKey(User,on_delete=models.CASCADE)
    # designation = models.CharField(max_length=30, null=True)
