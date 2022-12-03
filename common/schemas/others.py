import coreapi
from rest_framework.schemas.coreapi import AutoSchema
import coreschema


class MainGETSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        return self._manual_fields + api_fields


class ArticleListSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="ordering",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="order by: -created_at, created_at, -title, title"
                    ),
                ),
                coreapi.Field(
                    name="search",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="search by: title, description, title of parent, title of content(children)"
                    ),
                ),
                coreapi.Field(
                    name="rubric",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="filter by: news, article, science, instruction"
                    ),
                ),
            ]

        return self._manual_fields + api_fields


class ProductListSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="ordering",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="order by: -created_at, created_at, -title, title, -price, price"
                    ),
                ),
                coreapi.Field(
                    name="search",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="search by: title, description, value of characteristics"
                    ),
                ),
                coreapi.Field(
                    name="catalog__id",
                    required=False,
                    location="query",
                    schema=coreschema.String(description="filter by: catalog id"),
                ),
            ]

        return self._manual_fields + api_fields
