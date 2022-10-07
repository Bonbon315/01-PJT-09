# Generated by Django 3.2.13 on 2022-10-07 02:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='리뷰 내용'),
        ),
        migrations.AlterField(
            model_name='article',
            name='grade',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='평점'),
        ),
        migrations.AlterField(
            model_name='article',
            name='movie_name',
            field=models.CharField(max_length=50, verbose_name='영화 이름'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='리뷰 제목'),
        ),
    ]