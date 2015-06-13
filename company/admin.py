from django.contrib import admin
from company.models import Company, CompanyManager, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email', 'location',
                    'type', 'description', 'added_at', 'last_change']


@admin.register(CompanyManager)
class CompanyManagerAdmin(admin.ModelAdmin):
    list_display = ['company', 'manager']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'salary', 'added_at', 'last_change', 'company']
