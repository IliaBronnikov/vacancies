import datetime

import factory
from factory.fuzzy import FuzzyInteger, FuzzyText, FuzzyDate
from sites.models import Specialty, Company, Vacancy
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = FuzzyText()
    password = FuzzyText()


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = FuzzyText()
    location = FuzzyText()
    logo = factory.django.ImageField()
    description = FuzzyText()
    employee_count = FuzzyInteger(low=0)
    owner = factory.SubFactory(UserFactory)


class SpecialtyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Specialty

    title = FuzzyText()
    code = FuzzyText()
    picture = factory.django.ImageField()


class VacancyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vacancy

    title = factory.Sequence(lambda n: f"Vacancy {n}")
    company = factory.SubFactory(CompanyFactory)
    specialty = factory.SubFactory(SpecialtyFactory)
    skills = FuzzyText()
    description = FuzzyText()
    salary_min = FuzzyInteger(low=0)
    salary_max = FuzzyInteger(low=1)
    published_at = FuzzyDate(start_date=datetime.date(year=2000, month=1, day=1))
