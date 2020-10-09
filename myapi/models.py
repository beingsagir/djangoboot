from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=60)
    profession = models.CharField(max_length=60)
    def __str__(self):
        return self.name