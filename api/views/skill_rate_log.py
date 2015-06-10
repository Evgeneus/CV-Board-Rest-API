__all__ = ['SkillRateLogView']

from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.core.exceptions import PermissionDenied

from api.serializers import SkillRateLogSerializer
from helpers import IsUserOrAdmin


class SkillRateLogView(views.APIView):
    permission_classes = (IsAuthenticated, IsUserOrAdmin,)
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def post(self, request):
        user = request.user
        serializer = SkillRateLogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(user=user)
        except (IntegrityError, PermissionDenied):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
