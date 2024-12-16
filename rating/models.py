from enum import UNIQUE

from django.db import models
from author.models import Author
from post.models import Posts
from comment.models import Comments


class Rating(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)  # Связь с автором
    total_rating = models.IntegerField(default=0)

    def update_rating(self):
        """
        Recalculate the total rating for the associated author and update only the difference.
        """
        POST_RATING_MULTIPLIER = 3  # Константа для расчёта рейтинга постов

        if not self.author:
            raise ValueError("This rating instance is not associated with any author.")

        # 1. Считаем рейтинг всех постов автора
        post_ratings_sum = (
                                   Posts.objects.filter(author=self.author)
                                   .aggregate(total=models.Sum('post_rating'))['total'] or 0
                           ) * POST_RATING_MULTIPLIER

        # 2. Считаем рейтинг всех комментариев, которые оставил автор
        author_comment_ratings_sum = (
                Comments.objects.filter(author=self.author)
                .aggregate(total=models.Sum('comment_rating'))['total'] or 0
        )

        # 3. Считаем рейтинги всех комментариев под постами автора
        post_comment_ratings_sum = (
                Comments.objects.filter(post__author=self.author)
                .aggregate(total=models.Sum('comment_rating'))['total'] or 0
        )

        # Рассчитываем новый итоговый рейтинг
        new_total_rating = (
                post_ratings_sum + author_comment_ratings_sum + post_comment_ratings_sum
        )

        # Вычисляем разницу между старым и новым рейтингом
        delta = new_total_rating - self.total_rating

        # Обновляем существующий рейтинг только на дельту
        self.total_rating += delta
        self.save()

        return f"Total rating for author '{self.author}' updated successfully."


