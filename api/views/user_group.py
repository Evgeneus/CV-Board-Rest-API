__all__ = ['UserView', 'GroupViewset']

from django.contrib.auth.models import Group
from api.serializers import GroupSerializer
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from api.serializers import EditUserSerializer


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


class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
