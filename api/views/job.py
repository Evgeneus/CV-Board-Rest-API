__all__ = ['CreateJobView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from api.serializers import JobSerializer
from helpers.permitions import IsManagerOrAdmin
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
