from typing import Tuple, List
import uuid

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import CartItem, Cart, Order
from common.exceptions import *


# class CartService:
#     model = CartItem

#     # @classmethod
#     # def create_cart(cls, email: str, password: str) -> Tuple[User, Token, Token]:
#     #     user = authenticate(username=email, password=password)
#     #     if user:
#     #         token, created = cls.model.objects.get_or_create(user=user)
#     #         return user, token, created
#     #     else:
#     #         raise ObjectNotFoundException("User not found or not active")

#     @classmethod
#     def add_to_cart(cls, product: uuid, sum_amount_price: str, quantity: str) -> Cart:
#         item = cls.model(
#             product=product, quantity=quantity, sum_amount_price=sum_amount_price
#         )
#         Cart.objects.create(
#             items=[].append(item),
#             general_price=sum()

#         )

#     @classmethod
#     def destroy_auth_token(cls, user: User) -> None:
#         return cls.model.objects.filter(user=user).delete()

