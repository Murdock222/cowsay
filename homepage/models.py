from django.db import models

# Create your models here.
class MooText(models.Model):
    text = models.TextField()