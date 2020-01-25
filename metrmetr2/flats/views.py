from django.shortcuts import render

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
		houses = House.objects.filter(company_id=company_slug)
		houses_serialized = HousesSerializers(houses, many=True)

		return Response(houses_serialized.data)

# Один дом.
class HouseView(APIView):
	def get(self, request, company_slug, house_slug):
		houses = House.objects.filter(id=house_slug, company_id=company_slug)
		houses_serialized = HousesSerializers(houses, many=True)

		return Response(houses_serialized.data)
