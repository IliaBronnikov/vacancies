from pytest_factoryboy import register

from sites.tests.factories import (
    VacancyFactory,
    SpecialtyFactory,
    CompanyFactory,
    UserFactory,
)

register(VacancyFactory)
register(SpecialtyFactory)
register(CompanyFactory)
register(UserFactory)
