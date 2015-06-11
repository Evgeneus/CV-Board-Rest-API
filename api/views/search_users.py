__all__ = ['SearchUsersView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from haystack.query import SearchQuerySet

from api.serializers import SearchUsersSerializer


class SearchUsersView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        results = SearchQuerySet().all().values_list('location')

        return Response("ok", status=status.HTTP_200_OK)
