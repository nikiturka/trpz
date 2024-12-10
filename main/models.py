from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    position = models.CharField(max_length=255)
    health_status = models.TextField()

    def __str__(self):
        return self.name
