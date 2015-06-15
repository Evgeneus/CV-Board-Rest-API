__all__ = ['SearchUsersView', 'SearchCompanyView']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from haystack.query import SearchQuerySet

from extuser.models import ExtUser
from company.models import Company
from helpers import roles


class SearchUsersView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query_values = request.query_params.values()
        text = ''
        for value in query_values:
            text = text + ' ' + value

        if text:
            results = SearchQuerySet().filter(text=text)\
                                      .values('first_name', 'last_name',
                                              'email', 'desired_salary',
                                              'role', 'location',
                                              'register_date')\
                                      .models(ExtUser)
        else:
            results = SearchQuerySet().all().exclude(role=roles.ROLE_ADMIN)\
                                      .values('first_name', 'last_name',
                                              'email', 'desired_salary',
                                              'role', 'location',
                                              'register_date')\
                                      .models(ExtUser)

        results_list = []
        for result in results:
            results_list.append(result)

        return Response(results_list, status=status.HTTP_200_OK)


class SearchCompanyView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query_values = request.query_params.values()
        text = ''
        for value in query_values:
            text = text + ' ' + value

        if text:
            results = SearchQuerySet().filter(text=text)\
                                      .values('name', 'type',
                                              'email', 'address',
                                              'location', 'description',
                                              'added_at', 'last_change')\
                                      .models(Company)
        else:
            results = SearchQuerySet().all().exclude(role=roles.ROLE_ADMIN)\
                                      .values('name', 'type',
                                              'email', 'address',
                                              'location', 'description',
                                              'added_at', 'last_change')\
                                      .models(Company)

        results_list = []
        for result in results:
            results_list.append(result)

        return Response(results_list, status=status.HTTP_200_OK)
