"""vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from sites.views import (
    MainView,
    AllVacanciesView,
    VacanciesSpecView,
    CompanyCardView,
    VacancyDetailView,
)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", MainView.as_view(), name="index"),
    path("vacancies", AllVacanciesView.as_view(), name="vacancies"),
    path(
        "vacancies/cat/<str:speciality_code>",
        VacanciesSpecView.as_view(),
        name="vacancies_spec_view",
    ),
    path(
        "companies/<int:id_comp>", CompanyCardView.as_view(), name="vacancies_comp_view"
    ),
    path("vacancies/<int:id_vac>", VacancyDetailView.as_view(), name="vacancy"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
