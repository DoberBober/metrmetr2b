from django.contrib import admin

from .models import *


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

# Квартиры.
class ApartmentInline(admin.StackedInline):
    model = Apartment
    extra = 1
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'price',
                'square',
                'cost',
            ),
        }),
    )

# Дома.
class HouseAdmin(admin.ModelAdmin):
	search_fields = ['name']

	fieldsets = (
		(None, {
			'fields': (
				('name', 'slug', 'company')
			),
		}),
		(None, {
			'fields': (
				('district', 'completion', 'stage')
			),
		}),
	)

	list_display = ['name', 'company', 'district', 'completion', 'stage']
	inlines = [ApartmentInline]

admin.site.register(House, HouseAdmin)