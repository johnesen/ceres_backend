from collections import OrderedDict

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2, required=True)
    password = serializers.CharField(min_length=2, max_length=20, required=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=20, required=True)
    new_password = serializers.CharField(max_length=20, required=True, validators=[validate_password])
    confirm_new_password = serializers.CharField(max_length=20, required=True)

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResendActivationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ConfirmPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=8, max_length=20, required=True)
    confirm_new_password = serializers.CharField(min_length=8, max_length=20, required=True)


class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(min_length=2, required=True)
    email = serializers.EmailField(min_length=2, required=True, validators=[
        UniqueValidator(
            queryset=User.objects.all()
        )])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)



class UserSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    code = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_deleted = serializers.BooleanField(read_only=True)

