# Generated by Django 4.2 on 2023-07-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0021_alter_post_title2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title2',
            field=models.CharField(default='', max_length=200, verbose_name='Тақырып (каз)'),
        ),
    ]
