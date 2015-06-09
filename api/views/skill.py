__all__ = ['SetSkillView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from skills.models import SkillRate
from api.serializers import SkillRateSerializer


class SetSkillView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def patch(self, request):
        user = request.user
        skill_id = request.data.get('skill_id')

        try:
            int(skill_id)
        except ValueError:
            return Response({'detail': 'skill_id must be integer'},
                            status=status.HTTP_400_BAD_REQUEST)

        instance = get_object_or_404(SkillRate, user=user, skill=skill_id)

        serializer = SkillRateSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def post(self, request):
            user = request.user
            skill_id = request.data.get('skill_id')

            serializer = SkillRateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            try:
                serializer.save(user=user, skill=skill_id)
            except IntegrityError:
                return Response({'detail': 'object alredy exists'},
                                status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)