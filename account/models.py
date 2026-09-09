from django.db import models
from django.conf import settings

from core.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="کاربر",
    )
    first_name = models.CharField(verbose_name="نام", max_length=150, blank=True)
    last_name = models.CharField(
        verbose_name="نام خانوادگی", max_length=150, blank=True
    )
    avatar = models.ImageField(verbose_name="تصویر", upload_to="avatars/", blank=True)
    bio = models.TextField(verbose_name="درباره من", blank=True)
