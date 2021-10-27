import factory
from sites.models import Specialty, Company, Vacancy


class CompanyFactory(factory.Factory):
    class Meta:
        model = Company


class SpecialtyFactory(factory.Factory):
    class Meta:
        model = Specialty


class VacancyFactory(factory.Factory):
    class Meta:
        model = Vacancy

    company = factory.SubFactory(CompanyFactory)
    specialty = factory.SubFactory(SpecialtyFactory)
