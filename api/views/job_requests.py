__all__ = ['RequestFromUserView', 'RequestFromCompanyView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from jobrequest.models import RequestFromUser, RequestFromCompany
from company.models import Job
from extuser.models import ExtUser
from api.serializers import RequestFromUserSerializer, RequestFromCompanySerializer
from helpers.permitions import IsUserOrAdmin, IsManagerOrAdmin
from helpers.company_manager import is_manager_of_company


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


class RequestFromCompanyView(APIView):
    permission_classes = (IsManagerOrAdmin,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        manager = request.user
        users = RequestFromCompany.objects\
            .prefetch_related('job__company__company_manager')\
            .filter(job__company__company_manager__manager=manager)\
            .values()

        return Response(users, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RequestFromCompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        job_id = serializer.validated_data.get('job_id')
        job = get_object_or_404(Job, id=job_id)
        user_id = serializer.validated_data.get('user_id')
        user = get_object_or_404(ExtUser, id=user_id)
        company_id = job.company.id
        manager_id = request.user.id

        if is_manager_of_company(manager_id=manager_id, company_id=company_id):
            try:
                serializer.save(user=user, job=job)
            except IntegrityError:
                return Response({'detail': 'object alredy exists'},
                                status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_403_FORBIDDEN)
