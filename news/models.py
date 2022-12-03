from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel

class Rubric:
    news = "news"
    articles = "articles"
    science = "science"
    instruction = "instruction"

    @classmethod
    def choices(cls):
        return (
            (cls.articles, cls.articles),   
            (cls.news, cls.news),
            (cls.science, cls.science),
            (cls.instruction, cls.instruction),
        )


class Articles(BaseModel):
    title = models.CharField(
        max_length=150, blank=False, null=False, verbose_name=_("title")
    )
    description = models.TextField(
        blank=False, null=False, verbose_name=_("descriptions")
    )
    rubric = models.CharField(max_length=50, choices=Rubric.choices(), default=Rubric.articles)
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("parent"),
        related_name="contents",
    )

    class Meta:
        db_table = "articles"
        verbose_name = _("articles")
        verbose_name_plural = _("articles")


class ArticleMedia(BaseModel):
    article = models.ForeignKey(
        Articles,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("article"),
    )
    picture = models.ImageField(
        upload_to="article/%Y/%m/%d", blank=True, null=True, verbose_name=_("picture")
    )
    video = models.FileField(
        upload_to="article_video/%Y/%m/%d",
        blank=True,
        null=True,
        verbose_name=_("video"),
    )

    class Meta:
        db_table = "article_media"
        verbose_name = _("articles media")
        verbose_name_plural = _("articles media")
