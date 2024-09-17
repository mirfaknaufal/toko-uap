from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    time = models.DateField(default=timezone.now)
    description = models.TextField()
    genre = models.TextField()
    rating = models.CharField(max_length=255)