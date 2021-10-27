from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField()
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField()


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(
        Specialty, on_delete=models.CASCADE, related_name="vacancies"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="vacancies"
    )
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.IntegerField()
    written_cover_letter = models.CharField(max_length=1024)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name="applications"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )
