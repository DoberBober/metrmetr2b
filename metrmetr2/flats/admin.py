from django.contrib import admin
import nested_admin

from .models import *
from .forms import HouseForm, ApartmentForm, FloorForm


# Районы.
class DistrictAdmin(admin.ModelAdmin):
	search_fields = ['name']

	fieldsets = (
		(None, {
			'fields': (
				('name', 'slug')
			),
		}),
	)

	list_display = ['name', 'slug']

admin.site.register(District, DistrictAdmin)

# Строительные компании.
class CompanyAdmin(admin.ModelAdmin):
	search_fields = ['name']

	fieldsets = (
		(None, {
			'fields': (
				('name', 'slug')
			),
		}),
	)

	list_display = ['name', 'slug']

admin.site.register(Company, CompanyAdmin)

# Этапы строительства.
class StageAdmin(admin.ModelAdmin):
	search_fields = ['name']

	fieldsets = (
		(None, {
			'fields': (
				('name', 'slug')
			),
		}),
	)

	list_display = ['name', 'slug']

admin.site.register(Stage, StageAdmin)

# Этажи.
class FloorInline(nested_admin.NestedStackedInline):
	model = Floor
	form = FloorForm
	extra = 1
	classes = ['collapse', 'floors']
	fieldsets = (
		('Этажи', {
			# 'classes': ('collapse',),
			'fields': (
				('floor', 'price', 'cost',),
			),
		}),
	)

# Квартиры.
class ApartmentInline(nested_admin.NestedStackedInline):
	model = Apartment
	form = ApartmentForm
	classes = ['apartmentsBlock']
	extra = 1
	fieldsets = (
		('Показать/скрыть параметры квартиры', {
			'classes': ('collapse', 'apartments',),
			'fields': (
				'name', ('rooms', 'price'), ('square', 'cost'),
			),
		}),
	)
	
	inlines = [FloorInline]

# Дома.
class HouseAdmin(nested_admin.NestedModelAdmin):
	search_fields = ['name']
	form = HouseForm

	fieldsets = (
		(None, {
			'fields': (
				(('name', 'slug'), 'company')
			),
		}),
		(None, {
			'fields': (
				(('district', 'address'), ('completion', 'stage'))
			),
		}),
		(None, {
			'fields': (
				(('hirepurchase', 'mortgage', 'maternalcapital'),)
			),
		}),
		(None, {
			'fields': (
				('phone',)
			),
		}),
	)

	list_display = ['name', 'company', 'district', 'completion', 'stage']
	inlines = [ApartmentInline]

	def save_model(self, request, obj, form, change):
		if not obj.author:
			obj.author = request.user
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super(nested_admin.NestedModelAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(author=request.user)

admin.site.register(House, HouseAdmin)