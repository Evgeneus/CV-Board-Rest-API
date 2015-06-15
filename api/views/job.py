__all__ = ['CreateJobView', 'ManageJobView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.serializers import JobSerializer
from company.models import Job
from helpers.permitions import IsManagerOrAdmin, IsManagerOrAdminOrReadOnly
from helpers import roles, is_manager_of_company


class CreateJobView(APIView):
    permission_classes = (IsManagerOrAdmin,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        company_id = request.query_params.get('company_id')
        if is_manager_of_company(manager_id=request.user.id, company_id=company_id) \
                or request.user.role == roles.ROLE_ADMIN:
            serializer = JobSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(company_id=company_id)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class ManageJobView(APIView):
    permission_classes = (IsManagerOrAdminOrReadOnly,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, job_id):
        job = Job.objects.filter(id=job_id).values()

        return Response(job, status=status.HTTP_200_OK)

    def patch(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        company_id = job.company.id
        if is_manager_of_company(manager_id=request.user.id, company_id=company_id) \
                or request.user.role == roles.ROLE_ADMIN:
            serializer = JobSerializer(instance=job, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, job_id, format=None):
        job = get_object_or_404(Job, id=job_id)
        company_id = job.company.id
        if is_manager_of_company(manager_id=request.user.id, company_id=company_id) \
                or request.user.role == roles.ROLE_ADMIN:
            job.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)
