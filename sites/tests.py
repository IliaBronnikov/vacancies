import pytest
import datetime
from sites.factory import SpecialtyFactory, CompanyFactory, VacancyFactory
from django.test import TestCase
from sites.models import Specialty, Company, Vacancy
from sites.services import count_vacancies_by_speciality

# @pytest.mark.django_db()
# def test_count_vacancies_by_speciality():


@pytest.mark.django_db()
def test_count_vacancies_by_speciality():
    spec = Specialty.objects.create(code="huy", title="chlen")
    comp = Company.objects.create(
        name="a",
        location="b",
        logo="ads",
        description="234",
        employee_count=4,
    )
    Vacancy.objects.create(
        title="a",
        specialty=spec,
        company=comp,
        skills="243",
        description="5dsgf",
        salary_min="4325",
        salary_max="5365",
        published_at=datetime.datetime.now().date(),
    )
    Vacancy.objects.create(
        title="a",
        specialty=spec,
        company=comp,
        skills="243",
        description="5dsgf",
        salary_min="4325",
        salary_max="5365",
        published_at=datetime.datetime.now().date(),
    )

    count = count_vacancies_by_speciality("huy")

    assert count == 2
