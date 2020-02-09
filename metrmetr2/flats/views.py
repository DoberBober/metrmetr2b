from django.shortcuts import render
from django.db.models import Max

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Все дома и квартиры.
class AllApartmentsView(APIView):
	def get(self, request):
		houses = House.objects.all()
		houses_serialized = HousesSerializers(houses, many=True)

		return Response(houses_serialized.data)


# Одна компания.
class CompanyView(APIView):
	def get(self, request, company_slug):
		company_id = Company.objects.get(slug__iexact=company_slug).id

		houses = House.objects.filter(company_id=company_id)
		houses_serialized = HousesSerializers(houses, many=True)

		return Response(houses_serialized.data)

# Один дом.
class HouseView(APIView):
	def get(self, request, company_slug, house_slug):
		company_id = Company.objects.get(slug__iexact=company_slug).id
		house_id = House.objects.get(slug__iexact=house_slug).id

		houses = House.objects.filter(id=house_id, company_id=company_id)
		houses_serialized = HousesSerializers(houses, many=True)

		return Response(houses_serialized.data)

# Фильтр.
class FilterView(APIView):
	def get(self, request):
		maxPrice = Floor.objects.all().aggregate(Max('cost'))
		rooms_info = Apartment.objects.values_list('rooms', flat=True).distinct()
		stages = Stage.objects.all()
		stages_serialized = StagesFilterSerializers(stages, many=True).data
		districts = District.objects.all()
		districts_serialized = DistrictsFilterSerializers(districts, many=True).data
		companies = Company.objects.all()
		companies_serialized = CompaniesFilterSerializers(companies, many=True).data

		return Response({
			"maxPrice": maxPrice['cost__max'], 
			"rooms": rooms_info, 
			"stages": stages_serialized, 
			"districts": districts_serialized, 
			"companies": companies_serialized
		})