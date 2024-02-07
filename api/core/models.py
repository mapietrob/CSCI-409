from django.db import models

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=255)
    airport_code = models.CharField(max_length=3)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name