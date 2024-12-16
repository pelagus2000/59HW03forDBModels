from django.db import models
from post.models import Posts
from category.models import Category

class PostCategory(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
# Create your models here.



