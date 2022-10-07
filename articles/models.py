from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="리뷰 제목")
    content = models.TextField(verbose_name="리뷰 내용")
    movie_name = models.CharField(max_length=50, verbose_name="영화 이름")
    grade = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ],
        verbose_name="평점",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
