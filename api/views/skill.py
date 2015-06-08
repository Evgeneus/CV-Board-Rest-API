__all__ = ['SetSkillView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404

from skills.models import SkillRate
from api.serializers import SkillRateSerializer


class SetSkillView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def patch(self, request):
        user_id = request.user
        skill_id = request.data.get('skill_id')

        try:
            int(skill_id)
        except ValueError:
            return Response({'detail': 'skill_id must be integer'}, status=status.HTTP_400_BAD_REQUEST)

        instance = get_object_or_404(SkillRate, user_id=user_id, skill_id=skill_id)

        serializer = SkillRateSerializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
