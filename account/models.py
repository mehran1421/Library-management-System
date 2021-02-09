from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	email = models.EmailField(unique=True, verbose_name='ایمیل')
	slug = models.SlugField(unique=True, blank=True, verbose_name="کد کاربر")
	address=models.CharField(default='aaaa',max_length=200,verbose_name='آدرس')
