from django.db import models

# Create your models here.
STATE = (
	('b', 'Borrador'),
	('p', 'Publicado')
)

class Category(models.Model):
	nombre = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(db_index=True, editable=False)

	def __str__(self):
		return self.nombre


class Post(models.Model):
	slug = models.SlugField(unique=True,editable=False, default='')
	title = models.CharField(max_length = 120)	
	autor = models.CharField(max_length=100, default='admin')
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	state = models.CharField(max_length=1, choices=STATE, default='b')
	poster = models.ImageField(upload_to='posters_post/', null=True)
	category = models.ManyToManyField(Category)

	def __str__(self):
		return self.title