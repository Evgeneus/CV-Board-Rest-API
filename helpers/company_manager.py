__all__ = ['is_manager_of_company']


def is_manager_of_company(manager_id, company_id):
    from company.models import CompanyManager
    company_manager_entry = CompanyManager.objects.filter(manager=manager_id, company=company_id)
    if company_manager_entry:
        return True

    return False
