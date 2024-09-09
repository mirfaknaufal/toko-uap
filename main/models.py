from django.db import models

# Create your models here.
class StoreEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    genre = models.TextField()
    rating = models.CharField(max_length=255)