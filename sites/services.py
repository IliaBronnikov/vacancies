from django.db.models import Count

from sites.models import Vacancy, Specialty, Company


def build_specialities_context() -> dict:
    specs = []
    for spec in Specialty.objects.all().annotate(vacancies_count=Count("vacancies")):
        specs.append(
            {
                "title": spec.title,
                "code": spec.code,
                "count": spec.vacancies_count,
                "logo": spec.picture,
            }
        )
    return {"specialities": specs}


def build_companies_context() -> dict:
    companies = []
    for comp in Company.objects.all().annotate(vacancies_count=Count("vacancies")):
        companies.append(
            {
                "logo": comp.logo,
                "count": comp.vacancies_count,
                "id": comp.id,
            }
        )
    return {"companies": companies}


def get_field_of_company_model(id_comp: int, field: str):
    return getattr(Company.objects.get(id=id_comp), field)
