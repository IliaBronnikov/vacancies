from django.contrib import admin

# Register your models here.
from .models import Vacancy, Specialty, Company, Application

class VacancyAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Application, ApplicationAdmin)


