from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    time = models.DateField(default=timezone.now)
    description = models.TextField()
    genre = models.TextField()
    review = models.CharField(max_length=255)