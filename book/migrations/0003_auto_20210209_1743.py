# Generated by Django 3.1.6 on 2021-02-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210209_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(null=True, to='book.Category', verbose_name='دسته بندی'),
        ),
    ]
