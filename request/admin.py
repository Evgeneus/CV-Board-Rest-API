from django.contrib import admin
from request.models import RequestFromUser, RequestFromCompany


@admin.register(RequestFromUser)
class RequestFromUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'added_at']


@admin.register(RequestFromCompany)
class RequestFromCompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'added_at']
