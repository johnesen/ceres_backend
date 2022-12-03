from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class Catalog(BaseModel):
    title = models.CharField(
        max_length=150, blank=False, null=False, verbose_name=_("title")
    )
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("parent"),
        related_name="children",
    )
