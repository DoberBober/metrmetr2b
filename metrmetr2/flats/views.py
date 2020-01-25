from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class AllApartmentsView(APIView):
	def get(self, request):
		houses = House.objects.all()
		houses_serialized = HousesSerializers(houses, many=True)

		return Response(houses_serialized.data)