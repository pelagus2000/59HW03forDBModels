from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author_name = models.CharField(max_length=75, blank=False, default='Noname')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name

