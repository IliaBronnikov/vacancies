from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    name = models.CharField("название", max_length=64, null=True)
    location = models.CharField("название", max_length=64)
    logo = models.ImageField(
        "логотип",
    )
    description = models.TextField(
        "описание компании",
    )
    employee_count = models.IntegerField(
        "количество сотрудников",
    )
    owner = models.ForeignKey(User, verbose_name="владелец", on_delete=models.CASCADE)


class Specialty(models.Model):
    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    code = models.CharField("кодовое имя", max_length=64)
    title = models.CharField("специальность", max_length=64)
    picture = models.ImageField("логотип")


class Vacancy(models.Model):
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    title = models.CharField("название", max_length=64)
    specialty = models.ForeignKey(
        Specialty,
        verbose_name="специальность",
        on_delete=models.CASCADE,
        related_name="vacancies",
    )
    company = models.ForeignKey(
        Company,
        verbose_name="компания",
        on_delete=models.CASCADE,
        related_name="vacancies",
    )
    skills = models.TextField(
        "требуемые скиллы",
    )
    description = models.TextField(
        "описание вакансии",
    )
    salary_min = models.IntegerField(
        "минимум зарплаты",
    )
    salary_max = models.IntegerField(
        "максимум зарплаты",
    )
    published_at = models.DateField(
        "дата публикации",
    )


class Application(models.Model):
    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

    written_username = models.CharField("имя", max_length=64)
    written_phone = models.IntegerField(
        "номер телефона",
    )
    written_cover_letter = models.CharField("сопроводительное письмо", max_length=1024)
    vacancy = models.ForeignKey(
        Vacancy,
        verbose_name="вакансия",
        on_delete=models.CASCADE,
        related_name="applications",
    )
    user = models.ForeignKey(
        User,
        verbose_name="пользователь",
        on_delete=models.CASCADE,
        related_name="applications",
    )
