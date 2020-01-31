from .models import House, Apartment, Floor
from django.forms import ModelForm, TextInput

class HouseForm(ModelForm):
	class Meta:
		model = House
		fields = ['name', 'slug', 'address', 'completion', 'phone']
		widgets = {
			'name': TextInput(attrs={'class': 'vTextField', 'placeholder': 'Без «ЖК». Например, «Московский»'} ),
			'slug': TextInput(attrs={'class': 'vTextField', 'placeholder': 'moskovskiy'} ),
			'address': TextInput(attrs={'class': 'vTextField', 'placeholder': 'ул. Ленина, 1'} ),
			'completion': TextInput(attrs={'class': 'vIntegerField', 'placeholder': '2020'} ),
			'phone': TextInput(attrs={'class': 'vTextField', 'placeholder': '+7(000)111-22-33'} )
		}

class ApartmentForm(ModelForm):
	class Meta:
		model = Apartment
		fields = ['name', 'rooms', 'price', 'square', 'cost']
		widgets = {
			'name': TextInput(attrs={'class': 'vTextField', 'placeholder': 'Например, угловая квартира'} ),
			'rooms': TextInput(attrs={'class': 'vIntegerField', 'type': 'number', 'min': '1', 'placeholder': '1'} ),
			'price': TextInput(attrs={'class': 'vIntegerField', 'type': 'number', 'min': '1', 'placeholder': '30000'} ),
			'square': TextInput(attrs={'class': 'vIntegerField', 'type': 'number', 'min': '1', 'placeholder': '33,3'} ),
			'cost': TextInput(attrs={'class': 'vIntegerField', 'type': 'number', 'min': '1', 'placeholder': '999000'} )
		}

class FloorForm(ModelForm):
	class Meta:
		model = Floor
		fields = ['floor', 'price', 'cost']
		widgets = {
			'floor': TextInput(attrs={'class': 'vIntegerField', 'type': 'number', 'placeholder': '12'} ),
			'price': TextInput(attrs={'class': 'vIntegerField', 'type': 'number', 'min': '1', 'placeholder': '30000'} ),
			'cost': TextInput(attrs={'class': 'vIntegerField', 'type': 'number', 'min': '1', 'placeholder': '999000'} )
		}
