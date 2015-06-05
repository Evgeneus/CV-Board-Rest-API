__all__ = ['UserRegister']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from api.serializers import UserSerializer
from helpers import get_user_token


class UserRegister(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            credentials = {
                'email': serializer.validated_data['email'],
                'password': serializer.validated_data['password']
            }

            token = get_user_token(credentials)
            data = {'token': token}

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
