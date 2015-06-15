__all__ = ['CreateCompanyView', 'ManageCompanyView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.serializers import CompanySerializer
from company.models import Company
from helpers.permitions import IsManagerOrAdminOrReadOnly, IsManagerOrAdmin
from helpers import roles
from helpers.company_manager import is_manager_of_company


class CreateCompanyView(APIView):
    permission_classes = (IsManagerOrAdmin,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        manager = request.user
        serializer.save(manager=manager)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class ManageCompanyView(APIView):
    permission_classes = (IsManagerOrAdminOrReadOnly,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, company_id):
        company = Company.objects.filter(id=company_id).values()

        return Response(company, status=status.HTTP_200_OK)

    def patch(self, request, company_id):
        if is_manager_of_company(manager_id=request.user.id, company_id=company_id) \
                or request.user.role == roles.ROLE_ADMIN:
            instance = get_object_or_404(Company, id=company_id)
            serializer = CompanySerializer(instance=instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, company_id, format=None):
        if is_manager_of_company(manager_id=request.user.id, company_id=company_id) \
                or request.user.role == roles.ROLE_ADMIN:
            company = get_object_or_404(Company, id=company_id)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)
