import random
import uuid
from typing import Tuple, List

from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.db import transaction
from rest_framework.authtoken.models import Token

from .models import User
from common.exceptions import *

from common.message import my_message
from common.validators import validate_user_password


class TokenService:
    model = Token

    @classmethod
    def create_auth_token(cls, email: str, password: str) -> Tuple[User, Token, Token]:
        user = authenticate(username=email, password=password)
        if user:
            token, created = cls.model.objects.get_or_create(user=user)
            return user, token, created
        else:
            raise ObjectNotFoundException("User not found or not active")

    @classmethod
    def destroy_auth_token(cls, user: User) -> None:
        return cls.model.objects.filter(user=user).delete()


class UserService:
    model = User

    @classmethod
    def get(cls, **filters) -> User:
        return cls.model.objects.get(**filters)

    @classmethod
    def get_user(cls, **filters) -> User:
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException("User not found")

    @classmethod
    def filter_user(cls, **filters):
        return cls.model.objects.filter(**filters)

    @classmethod
    def exclude_user(cls, **filters):
        return cls.model.objects.exclude(**filters)

    @classmethod
    def check_user(cls, **filters) -> tuple:
        default_user = {"email": "", "username": ""}
        if filters.get("user"):
            default_user = filters.pop("user")
        return filters, default_user

    @classmethod
    def update_user(cls, user: User, email: str, username: str) -> User:
        if email:
            user.email = email
        if username:
            user.username = username
        user.save()
        return user

    @classmethod
    def create_user(
        cls, full_name: str, email: str, password: str, conf_password: str, **kwargs
    ) -> User:
        user = cls.model(full_name=full_name, email=email, **kwargs)
        correct_password = validate_user_password(
            password=password, conf_password=conf_password
        )
        user.set_password(correct_password)
        user.is_active = True
        user.save()
        return user

    @classmethod
    def change_password_user(
        cls, user: User, old_psw: str, new_psw: str, conf_new_psw: str
    ) -> User:
        user = cls.get_user(id=user.pk)
        if not user.check_password(raw_password=old_psw):
            raise IncorrectPasswordException("The current password is not correct")
        correct_new_password = validate_user_password(
            password=new_psw, conf_password=conf_new_psw
        )
        user.set_password(correct_new_password)
        user.save()
        return user

    # @classmethod
    # def check_code_and_update_password(
    #     cls, code: int, new_password: str, confirm_new_password: str
    # ):
    #     try:
    #         code = int(code)
    #         if new_password == confirm_new_password:
    #             if cls.model.objects.filter(code=code).exists():
    #                 user = cls.model.objects.get(code=code)
    #                 if user.is_active:
    #                     user.code = None
    #                     user.set_password(new_password)
    #                     user.save()
    #                 else:
    #                     raise ObjectNotFoundException("User is not activated")
    #             else:
    #                 raise IncorrectCodeException("Incorrect activation code")
    #         else:
    #             raise IncorrectPasswordException("Password mismatch")
    #     except ValueError:
    #         raise TypeErrorException("The code must be numeric")

    # @classmethod
    # def create_user_with_code(
    #     cls,
    #     full_name: str,
    #     email: str,
    #     password: str,
    #     conf_password: str,
    #     **kwargs
    # ) -> User:
    #     user = cls.model(full_name=full_name, email=email, **kwargs)
    #     correct_password = validate_user_password(
    #         password=password, conf_password=conf_password
    #     )

    #     user.code = SendEmailService.send_email(email)
    #     user.set_password(correct_password)
    #     user.save()
    #     return user

    # @classmethod
    # def resend_code(cls, email: str):
    #     if cls.model.objects.filter(email=email).exists():
    #         user = cls.model.objects.get(email=email)
    #         new_activation_code = SendEmailService.send_email(email)
    #         user.code = new_activation_code
    #         user.save()
    #     else:
    #         raise ObjectNotFoundException("User with this email was not found")


class SendEmailService:
    model = User

    @classmethod
    def activate_user(cls, code: str):
        try:
            code = int(code)
            if cls.model.objects.filter(code=code):
                user = cls.model.objects.get(code=code)
                user.is_active = True
                user.code = None
                user.save()
            else:
                raise IncorrectCodeException(
                    "Incorrect values or user has been activated"
                )
        except ValueError:
            raise TypeErrorException("The code must be numeric")

#     @staticmethod
#     def create_code():
#         activation_code = str(random.randint(100000, 999999))
#         return activation_code

#     @classmethod
#     def create_activation_code(cls, email: str):
#         activation_code = cls.create_code()
#         if not cls.model.objects.filter(code=activation_code).exists():
#             return activation_code
#         else:
#             return cls.create_activation_code(email)

#     @classmethod
#     def send_email(cls, email):
#         activation_code = cls.create_activation_code(email)
#         data = my_message(activation_code)
#         email = EmailMessage(
#             subject=data["email_subject"], body=data["email_body"], to=[email]
#         )
#         email.send()
#         return activation_code
