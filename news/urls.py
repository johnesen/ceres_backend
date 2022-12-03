from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListAPIView.as_view(), name='list-articles'),
]
      