from django.db import models

# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    job_position = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name
