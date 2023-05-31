from django.db import models
from django.contrib.auth.models import User
from club.models import Club

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rollno = models.IntegerField(null=False, default=0)
    semester = models.IntegerField()
    department = models.CharField(max_length=5)
    # joinedClub =  models.ManyToManyField(Club, null=True)

    @property
    def studentName(self):
            return f'{self.user.first_name} {self.user.last_name}'


