from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)          # Nazwa kursu
    scope = models.CharField(max_length=200)         # Zakres
    location = models.CharField(max_length=100)      # Miejscowość
    date = models.DateField()                        # Data

    def __str__(self):
        return self.name