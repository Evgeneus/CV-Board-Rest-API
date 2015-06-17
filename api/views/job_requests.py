__all__ = ['RequestFromUserView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from jobrequest.models import RequestFromUser
from company.models import Job
from helpers.permitions import IsUserOrAdmin
from api.serializers import RequestFromUserSerializer


class RequestFromUserView(APIView):
    permission_classes = (IsUserOrAdmin,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        user = request.user
        job_id = request.query_params.get('job_id')
        if job_id:
            job = get_object_or_404(Job, id=job_id)
            job_requests = RequestFromUser.objects.filter(user=user, job=job).values()
        else:
            job_requests = RequestFromUser.objects.filter(user=user).values()

        return Response(job_requests, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        serializer = RequestFromUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(user=user)
        except IntegrityError:
            return Response({'detail': 'object alredy exists'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = {'user_id': user.id, 'job_id': serializer.validated_data.get('job_id')}

        return Response(data, status=status.HTTP_200_OK)
