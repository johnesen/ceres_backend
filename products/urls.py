from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='list-products'),
    path('carts/', views.CartItemAPIView.as_view(), name='create-cart'),
]
      