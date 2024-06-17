# Generated by Django 4.2 on 2023-07-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0015_alter_postimage_post_alter_postlink_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Ссылка (автосоздание)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
