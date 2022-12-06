from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='list-products'),
    path('cart-item/', views.CartItemAPIView.as_view(), name='create-cart-item'),
    path('carts/', views.CartAPIView.as_view(), name='create-cart'),
]
      