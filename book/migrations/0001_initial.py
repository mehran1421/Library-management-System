# Generated by Django 3.1.6 on 2021-02-09 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=100, verbose_name='موضوع')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slugBook', models.SlugField(blank=True, unique=True, verbose_name='کد کتاب')),
                ('slugUser', models.SlugField(blank=True, unique=True, verbose_name='کد کاربر')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('renewCount', models.IntegerField(verbose_name='تعداد تمدید')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='تایتل')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='کد کتاب')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('author', models.CharField(max_length=200, verbose_name='نویسنده')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='عکس')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('status', models.CharField(choices=[('d', 'امانت گرفته شده'), ('p', 'موجود')], max_length=1, verbose_name='وضعیت')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب ها',
                'ordering': ['-created'],
            },
        ),
    ]