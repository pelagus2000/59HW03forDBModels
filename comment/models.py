from django.db import models

from post.models import Posts
from author.models import Author


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)


    def comment_like(self):
        self.comment_rating += 1
        self.save()

    def comment_dislike(self):
        self.comment_rating -= 1
        self.save()


