from django.shortcuts import render
from django.views import View
from sites.services import *
from sites.models import Vacancy


class MainView(View):
    def get(self, request, *args, **kwargs):
        specialities_context = build_specialities_context()
        companies_context = build_companies_context()
        return render(
            request,
            "index.html",
            context={
                **specialities_context,
                **companies_context,
            },
        )


class AllVacanciesView(View):
    def get(self, request, *args, **kwargs):
        number_of_vacations = Vacancy.objects.count()
        all_vacancies = Vacancy.objects.all()
        return render(
            request,
            "full_lst_vacancies.html",
            context={"quantity": number_of_vacations, "data": all_vacancies},
        )


class VacanciesSpecView(View):
    def get(self, request, speciality_code, *args, **kwargs):
        speciality = Specialty.objects.get(code=speciality_code).title
        number_of_vacations_by_speciality = Vacancy.objects.filter(
            specialty__code=speciality_code
        ).count()
        all_vacancies_by_speciality = Vacancy.objects.filter(
            specialty__code=speciality_code
        )
        return render(
            request,
            "vacancies_for_speciality.html",
            context={
                "speciality": speciality,
                "quantity": number_of_vacations_by_speciality,
                "data": all_vacancies_by_speciality,
            },
        )


class CompanyCardView(View):
    def get(self, request, id_comp, *args, **kwargs):
        number_of_vacations_by_company = Vacancy.objects.filter(
            company__id=id_comp
        ).count()
        company_name = get_field_of_company_model(id_comp, "name")
        company_logo = get_field_of_company_model(id_comp, "logo")
        all_vacancies_by_company = Vacancy.objects.filter(company__id=id_comp)
        return render(
            request,
            "company.html",
            context={
                "quantity": number_of_vacations_by_company,
                "data": all_vacancies_by_company,
                "logo": company_logo,
                "name": company_name,
            },
        )


class VacancyDetailView(View):
    def get(self, request, id_vac, *args, **kwargs):
        vacancy_data = Vacancy.objects.get(id=id_vac)
        return render(request, "vacancy.html", context={"vacancy": vacancy_data})


class ApplicationView(View):
    def post(self, request, id_vac, *args, **kwargs):
        written_username = request.user.userName
        written_phone = request.user.userPhone
