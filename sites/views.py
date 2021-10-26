from django.shortcuts import render
from django.views import View
from sites.services import *
from sites.models import Vacancy
from collections import defaultdict
from django.shortcuts import redirect




class MainView(View):
    def get(self, request, *args, **kwargs):
        all_vacancies_divided_by_specialities = count_vacancies_by_all_specialities()
        all_vacancies_divided_by_company = count_vacancies_by_all_company()
        return render(request, 'index.html', context={'specialities': all_vacancies_divided_by_specialities,
                      'company': all_vacancies_divided_by_company})


class AllVacanciesView(View):
    def get(self, request, *args, **kwargs):
        quantity = count_all_vacancies()
        all_vacancies = Vacancy.objects.all()
        return render(request, 'full_lst_vacancies.html', context={"quantity": quantity, 'data': all_vacancies})


class VacanciesSpecView(View):
    def get(self, request, category, *args, **kwargs):
        cat_of_vacancies = title_of_specialty(category)
        quantity_vacancies_by_specialitie = count_vacancies_by_specialitie(category)
        all_vacancies_for_speciality = Vacancy.objects.filter(specialty__code=category)
        return render(request, 'vacancies_for_speciality.html', context={'cat_of_vacancies': cat_of_vacancies,
                'quantity': quantity_vacancies_by_specialitie, 'data': all_vacancies_for_speciality})


class CompanyCardView(View):
    def get(self, request, id_comp, *args, **kwargs):
        quantity = count_vacancies_by_company(id_comp)
        company_name = get_field_of_company_model(id_comp, 'name')
        company_logo = get_field_of_company_model(id_comp, 'logo')
        all_vacancies_for_company = lst_vacancies_for_company(id_comp)
        return render(request, 'company.html', context={"quantity": quantity, 'data': all_vacancies_for_company,
                                                        'logo': company_logo, 'name': company_name})


class VacancyDetailView(View):
    def get(self, request, id_vac, *args, **kwargs):
        vacancy_data = Vacancy.objects.get(id=id_vac)
        return render(request, 'vacancy.html', context={'data': vacancy_data})


class ApplicationView(View):
    def post(self, request, id_vac, *args, **kwargs):
        written_username = request.user.userName
        written_phone = request.user.userPhone



