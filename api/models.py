from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True)

    token = models.CharField(verbose_name="用户TOKEN", max_length=64, blank=True, null=True)