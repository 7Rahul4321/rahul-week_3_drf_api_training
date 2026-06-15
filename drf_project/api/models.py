from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()

    def _str_(self):
        return self.name