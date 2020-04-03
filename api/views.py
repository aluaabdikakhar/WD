from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from api.models import Company, Vacancy

companies_list = Company.objects.all() #выводит список всех компаний
companies_list_json = [p.to_json() for p in companies_list] # и выводит в json формате

def companies(request):
    return JsonResponse(companies_list_json, safe = False)

def company(request, id):

   try:

      company_detail = Company.objects.get(id = id)

   except Company.DoesNotExist:

      return JsonResponse({'error': 'company does not exists'})

   return JsonResponse(company_detail.to_json())

def vacancies(request):

   vacancy_list = Vacancy.objects.all()

   vacancy_list_json = [c.to_json() for c in vacancy_list]

   return JsonResponse(vacancy_list_json, safe=False)

def vacancy(request, id):

   try:

      vacancy_detail = Vacancy.objects.get(id=id)

   except Vacancy.DoesNotExist:

      return JsonResponse({'error': 'vacancy does not exists'})

   return JsonResponse(vacancy_detail.to_json())

def vacancy_products(request, id):

   if id == 1:

      companies = companies_list_json[:5]

      return JsonResponse(companies, safe = False)

   elif id == 2:

      companies = companies_list_json[5:10]

      return JsonResponse(companies, safe=False)

   else:

      companies = companies_list_json[10:15]
      return JsonResponse(companies, safe=False)

# Create your views here.

