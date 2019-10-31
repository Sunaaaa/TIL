from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=30)
    past_job = models.TextField()

    # def __str__(self):
    #     return f'[{}]'