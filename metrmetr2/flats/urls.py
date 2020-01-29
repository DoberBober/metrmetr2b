from django.urls import path

from .views import *

urlpatterns = [
	path('api/v0/all', AllApartmentsView.as_view(), name='all_apartments_url'),
	path('api/v0/filter', FilterView.as_view(), name='filter_url'),
	path('api/v0/<company_slug>', CompanyView.as_view(), name='company_apartments_url'),
	path('api/v0/<company_slug>/<house_slug>', HouseView.as_view(), name='house_apartments_url'),
]