# Generated by Django 4.2 on 2023-07-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
