from django.urls import path

from .views import *

urlpatterns = [
	path('api/v0/all/', AllApartmentsView.as_view(), name='all_aprtments_url'),
]