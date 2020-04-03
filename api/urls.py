from django.urls import path
from api.views import companies, company, vacancies, vacancy, vacancy_products

urlpatterns = [
    path('companies/', companies),
    path('companies/<int:id>/', company),
    path('companies/<int:id>/vacancies/', vacancy_products),
    path('vacancies/', vacancies),
    path('vacancies/<int:id>/', vacancy)
]