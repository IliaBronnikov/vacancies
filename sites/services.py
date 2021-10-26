from sites.models import Vacancy, Specialty, Company


def count_vacancies_by_speciality(code: str) -> int:
    return Vacancy.objects.filter(specialty__code=code).count()

def count_vacancies_by_all_specialities() -> dict:
    all_vacancies_divided_by_specialities = {}
    counter = 1
    for item in Specialty.objects.values_list('title', flat=True).distinct():
        all_vacancies_divided_by_specialities[counter] = {"title": str(item), "code": 'vacancies/cat/' +
            str(Specialty.objects.filter(title=item).values_list('code')[0][0]), "count":Vacancy.objects.filter(
            specialty__title=item).count(), "logo": Specialty.objects.filter(title=item).values_list('picture')[0][0]}
        counter += 1
    return all_vacancies_divided_by_specialities

def count_vacancies_by_all_company() -> dict:
    all_vacancies_divided_by_company = {}
    counter = 1
    for item in Company.objects.values_list('name', flat=True).distinct():
        all_vacancies_divided_by_company[counter] = {"logo":Company.objects.filter(
            name=item).values_list('logo')[0][0], "count":Vacancy.objects.filter(company__name=item).count(),
            "id": 'companies/' + str(Company.objects.filter(name=item).values_list('id')[0][0])}
        counter += 1
    return all_vacancies_divided_by_company

def comparing_logo_vacancies() -> dict:
    all_logs_for_vacancies = {}
    for item in Vacancy.objects.all():
        all_logs_for_vacancies[item.title] = '../static/company/' + Company.objects.filter(
            pk=item.company_id).values_list('logo')[0][0]
    return all_logs_for_vacancies

def title_of_specialty(category: str) -> str:
    return Specialty.objects.filter(code=category).values_list('title')[0][0]

def count_vacancies_by_specialitie(category: str) -> int:
    return Vacancy.objects.filter(specialty__code=category).count()

def count_vacancies_by_company(id_comp: int) -> int:
    return Vacancy.objects.filter(company__id=id_comp).count()

def count_all_vacancies() -> int:
    return Vacancy.objects.count()

def lst_vacancies_for_company(id_comp: int) -> dict:
    return Vacancy.objects.filter(company__id=id_comp)

def get_field_of_company_model( id_comp: int, field: str):
    return getattr(Company.objects.get(id=id_comp), field)