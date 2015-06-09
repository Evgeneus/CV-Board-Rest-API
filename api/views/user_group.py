__all__ = ['UserView', 'GetUsersView', 'GroupViewset']

from django.contrib.auth.models import Group
from api.serializers import GroupSerializer
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from api.serializers import EditUserSerializer
from extuser.models import ExtUser
from helpers import roles


class UserView(views.APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def patch(self, request):
        user = request.user

        serializer = EditUserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        user = request.user
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class GetUsersView(views.APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        role = int(request.query_params.get('role'))

        if role == roles.ROLE_USER:
            users = ExtUser.objects.filter(role=roles.ROLE_USER)\
                .values('first_name', 'last_name', 'email',
                        'date_of_birth', 'is_active', 'role',
                        'age', 'desired_salary', 'register_date',
                        'last_change', 'location', 'other')

        elif role == roles.ROLE_MANAGER:
            users = ExtUser.objects.filter(role=roles.ROLE_MANAGER)\
                .values('first_name', 'last_name', 'email',
                        'date_of_birth', 'is_active', 'role',
                        'age', 'desired_salary', 'register_date',
                        'last_change', 'location', 'other')

        else:
            users = ExtUser.objects.exclude(role=roles.ROLE_ADMIN)\
                .values('first_name', 'last_name', 'email',
                        'date_of_birth', 'is_active', 'role',
                        'age', 'desired_salary', 'register_date',
                        'last_change', 'location', 'other')

        return Response(users)


class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
