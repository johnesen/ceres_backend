from django.urls import path
from . import views

urlpatterns = [
    path('catalogs/', views.CatalogsListAPIView.as_view(), name='catalog list'),
]
      