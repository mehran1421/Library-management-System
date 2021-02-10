# Generated by Django 3.1.6 on 2021-02-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210209_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='applying_renew',
            field=models.CharField(choices=[('a', 'درخواست تمدید'), ('b', 'درحال پیگیری'), ('c', 'موافقت تمدید'), ('e', 'مخالفت تمدید')], default='a', max_length=1, verbose_name='وضعیت'),
        ),
    ]