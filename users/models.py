from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel
from .managers import BaseUserManager
from django.db import models
from .permissions import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    full_name = models.CharField(
        max_length=150, blank=False, null=False, verbose_name=_("full name")
    )
    email = models.EmailField(
        blank=False, null=False, unique=True, verbose_name=_("email address")
    )
    password = models.CharField(
        max_length=128, blank=True, null=True, verbose_name=_("passowrd")
    )
    code = models.PositiveIntegerField(
        null=True, unique=True, verbose_name=_("activation code")
    )
    is_superuser = models.BooleanField(
        default=False, blank=True, verbose_name=_("is admin user?")
    )
    is_active = models.BooleanField(
        default=False, blank=True, verbose_name=_("is active?")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("-created_at",)
