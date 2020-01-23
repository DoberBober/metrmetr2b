from django.db import models
from django.utils.text import slugify

class PublicationMixin(models.Model):
	publication = models.BooleanField(verbose_name="Опубликовать", default=1)

	class Meta:
		abstract = True

# Функция генерации слага.
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'i', 'ь': '',
            'э': 'e', 'ю': 'yu', 'я': 'ya'}

def gen_slug(s):
	new_slug = slugify(''.join(alphabet.get(w, w) for w in s.lower()))
	return new_slug