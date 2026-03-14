from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to="profile", null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.user.username

class Recruiter(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        mobile = models.CharField(max_length=15, null=True)
        image = models.FileField(upload_to="profile", null=True)
        type = models.CharField(max_length=20, null=True)
        gender = models.CharField(max_length=10, null=True)
        company = models.CharField(max_length=200, null=True)
        status = models.CharField(max_length=20, null=True)

        def __str__(self):
            return self.user.username


class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=15, null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=20, null=True)
    salary = models.FloatField(max_length=10, null=True)
    image = models.ImageField(upload_to="job_images", null=True)
    description = models.CharField(max_length=200, null=True)
    experience = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, null=True)
    skills = models.CharField(max_length=50, null=True)
    creation_date = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title


