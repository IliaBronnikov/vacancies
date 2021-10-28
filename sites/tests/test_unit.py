from sites.services import build_specialities_context, build_companies_context
import pytest


@pytest.mark.django_db()
def test_build_specialities_context(vacancy_factory, specialty_factory):
    spec1 = specialty_factory()
    spec2 = specialty_factory()
    vacancy_factory(specialty=spec2)

    context = build_specialities_context()

    assert "specialities" in context
    assert len(context["specialities"]) == 2
    assert context["specialities"][0] == {
        "title": spec1.title,
        "code": spec1.code,
        "count": 0,
        "logo": spec1.picture,
    }
    assert context["specialities"][1] == {
        "title": spec2.title,
        "code": spec2.code,
        "count": 1,
        "logo": spec2.picture,
    }


@pytest.mark.django_db()
def test_build_companies_context(vacancy_factory, company_factory):
    comp1 = company_factory()
    comp2 = company_factory()
    vacancy_factory(company=comp1)

    context = build_companies_context()

    assert "companies" in context
    assert len(context["companies"]) == 2
    assert context["companies"][0] == {
        "logo": comp1.logo,
        "count": 1,
        "id": comp1.id,
    }
    assert context["companies"][1] == {
        "logo": comp2.logo,
        "count": 0,
        "id": comp2.id,
    }
