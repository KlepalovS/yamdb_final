# Generated by Django 3.2 on 2023-02-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_remove_review_unique_author_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.FloatField(blank=True, null=True, verbose_name='Рейтинг'),
        ),
    ]