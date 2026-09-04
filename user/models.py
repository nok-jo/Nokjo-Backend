from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from core.models import TimeStampedModel
from .validators import phone_validator


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone, password, **extra_field):
        if not phone:
            raise ValueError("The number cannot empty!")
        user = self.model(phone=phone, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_field):
        extra_field.setdefault("is_active", True)
        extra_field.setdefault("is_staff", False)
        return self._create_user(phone, password, **extra_field)

    def create_superuser(self, phone, password=None, **extra_field):
        extra_field.setdefault("is_active", True)
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)

        if extra_field.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_field.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(phone, password, **extra_field)


class CustomUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    phone = models.CharField(
        verbose_name="شماره",
        max_length=20,
        unique=True,
        validators=[phone_validator],
        help_text="شماره باید منحصر به فرد باشد.",
    )
    nickname = models.CharField(max_length=30, unique=True, verbose_name="نام مستعار")
    is_active = models.BooleanField(
        default=True, help_text="مشخص میکند آیا کاربر فعال است یا نه"
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="مشخص میکند آیا این کاربر میتواند وارد پنل ادمین شود یا نه",
    )

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربرها"

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["nickname"]

    objects = CustomUserManager()

    def __str__(self):
        return self.nickname
