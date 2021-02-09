from django.db import models
from django.utils import timezone

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
    title=models.CharField(max_length=200, verbose_name="تایتل")
    slug = models.SlugField(blank=True, verbose_name="عنوان")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL,verbose_name="دسته بندی")
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to='images', verbose_name="عکس")
    created = models.DateTimeField(auto_now_add=True,verbose_name='زمان انتشار')
    status = models.CharField(max_length=1, choices=Status_Choise, verbose_name="وضعیت")

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"
        ordering = ['-created']

    def __str__(self):
        return self.title