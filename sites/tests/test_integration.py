import pytest
from django.urls import reverse


@pytest.mark.django_db()
def test_index_page(client, vacancy):
    index_url = reverse("index")

    response = client.get(index_url)
    content = response.content.decode("utf-8")

    assert response.status_code == 200
    assert "Вакансии для <br>Junior-разработчиков" in content
    assert vacancy.specialty.title in content
    assert vacancy.company.logo.url in content


@pytest.mark.django_db()
def test_vacancy_page(client, vacancy):
    vacancy_url = reverse("vacancy", kwargs={"id_vac": 1})

    response = client.get(vacancy_url)
    content = response.content.decode("utf-8")

    assert response.status_code == 200
    assert "Отозваться на вакансию" in content
    assert vacancy.company.name in content
    assert vacancy.company.location in content
