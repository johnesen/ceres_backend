from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .services import *
from common.permissions import *
from common.schemas.users import *

# from common.utils import get_instance_slice


class RegisterAPIView(generics.GenericAPIView):

    permission_classes = (AllowAny,)
    schema = UserRegisterSchema()
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserService.create_user(
            full_name=serializer.validated_data.get("full_name"),
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
            conf_password=serializer.validated_data.get("confirm_password"),
        )
        user, token, _ = TokenService.create_auth_token(
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
        )
        return Response(
            data={
                "message": "The user has been successfully created",
                "data": {
                    "token": str(token),
                    "token_type": "Token",
                    "user": UserSerializer(user).data,
                },
                "status": "CREATED",
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    schema = LoginSchema()
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token, _ = TokenService.create_auth_token(
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
        )
        return Response(
            data={
                "message": "You have successfully logged in",
                "data": {
                    "token": str(token),
                    "token_type": "Token",
                    "user": UserSerializer(user).data,
                },
                "status": "OK",
            },
            status=status.HTTP_200_OK,
        )

   