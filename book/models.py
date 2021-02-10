from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from account.models import User


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, verbose_name="موضوع")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title


class Book(models.Model):
    Status_Choise = (
        ('d', 'امانت گرفته شده'),
        ('p', 'موجود'),
    )
    title = models.CharField(max_length=200, verbose_name="تایتل")
    slug = models.SlugField(unique=True, blank=True, verbose_name="کد کتاب")
    category = models.ManyToManyField(Category, null=True, verbose_name="دسته بندی")
    description = models.TextField(verbose_name="توضیحات")
    author = models.CharField(max_length=200, verbose_name="نویسنده")
    thumbnail = models.ImageField(upload_to='images', verbose_name="عکس")
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')
    status = models.CharField(max_length=1, choices=Status_Choise, verbose_name="وضعیت")

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"
        ordering = ['-created']

    def __str__(self):
        return self.title

    def category_to_string(self):
        return ", ".join([cat.title for cat in self.category.all()])

    category_to_string.short_description = "دسته بندی"


class Issue(models.Model):
    slugBook = models.SlugField(unique=True, blank=True, verbose_name="کد کتاب")
    slugUser = models.SlugField(unique=True, blank=True, verbose_name="کد کاربر")
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')
    renewCount = models.IntegerField(verbose_name="تعداد تمدید")
    class Meta:
        verbose_name = "امانت"
        verbose_name_plural = "امانات"
        ordering = ['-created']

    def __str__(self):
        return self.slugUser + ' : ' + self.slugBook

    def is_on_time(self):
        last_two_week = timezone.now() - timedelta(days=14)
        if self.created > last_two_week:
            return True
        else:
            return False

    is_on_time.boolean = True
    is_on_time.short_description = "وضعیت کتاب به امانت گرفته شده"
