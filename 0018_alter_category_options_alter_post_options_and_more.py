# Generated by Django 4.2 on 2023-07-27 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0017_alter_postimage_options_alter_postlink_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория / Санат', 'verbose_name_plural': 'Категории / Санаттар'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('title',), 'verbose_name': 'Новость / Жаңалықтар', 'verbose_name_plural': 'Новости / Жаңалықтар'},
        ),
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Изображение / Сурет', 'verbose_name_plural': 'Изображения / Суреттер'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Имя категории / Санат атауы'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='mySite.category', verbose_name='Категория / Санат'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post/%Y/%m/%d', verbose_name='Главное фото / Негізгі сурет'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации / Жарияланған күні'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок / Тақырып'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления / Жаңарту күні'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='post/%Y/%m/%d/', verbose_name='Дополнительное фото / Қосымша фотосурет'),
        ),
    ]
