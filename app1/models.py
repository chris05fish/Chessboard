from django.db import models

# Create your models here.
class Board(models.Model):
    Source = models.CharField(max_length=2, primary_key=True)
    Destination = models.CharField(max_length=6)
