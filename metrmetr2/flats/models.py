from django.db import models
from .utils import PublicationMixin, gen_slug


# Район.
class District(models.Model):
	name = models.CharField(max_length=150, verbose_name="Район")
	slug = models.SlugField(max_length=150, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = gen_slug(self.name)
				
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		db_table = 'tbl_districts'
		verbose_name = 'Район'
		verbose_name_plural = 'Районы'

# Строительная компания.
class Company(models.Model):
	name = models.CharField(max_length=150, verbose_name="Строительная компания")
	slug = models.SlugField(max_length=150, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = gen_slug(self.name)
				
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		db_table = 'tbl_companies'
		verbose_name = 'Строительная компания'
		verbose_name_plural = 'Строительные компании'

# Этап строительства.
class Stage(models.Model):
	name = models.CharField(max_length=150, verbose_name="Этап строительства")
	slug = models.SlugField(max_length=150, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = gen_slug(self.name)
				
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		db_table = 'tbl_stages'
		verbose_name = 'Этап строительства'
		verbose_name_plural = 'Этапы строительства'

# Дом.
class House(models.Model):
	name = models.CharField(max_length=150, verbose_name="Название ЖК")
	slug = models.SlugField(max_length=150, unique=True, blank=True)
	district = models.ForeignKey(District, related_name='house_district', null=True, on_delete=models.SET_NULL, verbose_name="Район")
	address = models.CharField(max_length=250, blank=True, verbose_name="Адрес")
	company = models.ForeignKey(Company, related_name='house_owner', null=True, on_delete=models.SET_NULL, verbose_name="Строительная компания")
	completion = models.IntegerField(verbose_name="Год завершения строительства")
	stage = models.ForeignKey(Stage, related_name='house_stage', null=True, on_delete=models.SET_NULL, verbose_name="Этап строительства")
	hirepurchase = models.BooleanField(default=0, verbose_name='Рассрочка')
	mortgage = models.BooleanField(default=0, verbose_name='Ипотека')
	maternalcapital = models.BooleanField(default=0, verbose_name='Материнский капитал')

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = gen_slug(self.name)
				
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		db_table = 'tbl_houses'
		verbose_name = 'ЖК'
		verbose_name_plural = 'ЖК'

# Квартира.
class Apartment(models.Model):
	name = models.CharField(max_length=150, verbose_name="Название")
	house = models.ForeignKey(House, related_name='apartment_house', null=True, on_delete=models.SET_NULL, verbose_name="ЖК")
	rooms = models.IntegerField(verbose_name="Количество комнат")
	price = models.IntegerField(verbose_name="Стоимость квадратного метра")
	cost = models.IntegerField(verbose_name="Цена квартиры")
	square = models.IntegerField(verbose_name="Площадь")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['rooms']
		db_table = 'tbl_apartments'
		verbose_name = 'Квартира'
		verbose_name_plural = 'Квартиры'

# Этаж.
class Floor(models.Model):
	apartment = models.ForeignKey(Apartment, related_name='floor_apartment', null=True, on_delete=models.SET_NULL, verbose_name="Квартира")
	floor = models.IntegerField(verbose_name="Этаж")
	price = models.IntegerField(verbose_name="Стоимость квадратного метра", null=True, blank=True)
	cost = models.IntegerField(verbose_name="Цена квартиры", null=True, blank=True)

	def __str__(self):
		return "Этаж " + str(self.floor)

	class Meta:
		ordering = ['floor']
		db_table = 'tbl_floors'
		verbose_name = 'Этаж'
		verbose_name_plural = 'Этажи'