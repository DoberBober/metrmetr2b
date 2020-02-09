from .models import *
from rest_framework import serializers


class FloorSerializers(serializers.ModelSerializer):
	class Meta:
		model = Floor
		fields = ("id", "floor", "price", "cost")


class ApartmentSerializers(serializers.ModelSerializer):
	floors = FloorSerializers(many=True, source='floor_apartment')
	
	class Meta:
		model = Apartment
		fields = ("id", "name", "rooms", "price", "cost", "square", "floors")


class HousesSerializers(serializers.ModelSerializer):
	district = serializers.CharField(source="district.name", read_only=True)
	company = serializers.CharField(source="company.name", read_only=True)
	stage = serializers.CharField(source="stage.name", read_only=True)
	apartments = ApartmentSerializers(many=True, source='apartment_house')
	
	class Meta:
		model = House		
		fields = ("id", "name", "slug", "address", "completion", "hirepurchase", "mortgage", "maternalcapital", "phone", "district", "company", "stage", "apartments")


# Для фильтра.
class StagesFilterSerializers(serializers.ModelSerializer):
	class Meta:
		model = Stage
		fields = ("id", "name")

class DistrictsFilterSerializers(serializers.ModelSerializer):
	class Meta:
		model = District
		fields = ("id", "name")

class CompaniesFilterSerializers(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ("id", "name")
