# Generated by Django 4.2 on 2023-07-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0016_alter_category_slug_alter_post_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='postlink',
            options={'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Имя категории'),
        ),
    ]
