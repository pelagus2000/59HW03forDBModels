from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)
