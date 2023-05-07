from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models
    rollno = models.IntegerField(null=False, default=0)
    semester = models.IntegerField()
    department = models.CharField(max_length=5)
    # joinedClub = models.ForeignKey()
