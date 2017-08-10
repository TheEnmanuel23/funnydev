from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

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

class Author( models.Model ):
	name = models.CharField(max_length=120)
	link = models.CharField(max_length=400, blank=True, default='#')

	def __str__(self):
		return self.name

class Post(models.Model):
	slug = models.SlugField(editable=False, default='')
	title = models.CharField(max_length = 120)	
	content = RichTextUploadingField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	state = models.CharField(max_length=1, choices=STATE, default='b')
	description = models.CharField(max_length=2000, default='')
	author = models.ForeignKey(Author)
	category = models.ManyToManyField(Category)
	poster = models.ImageField(upload_to='post_resources/', null=True, blank=True)	
	colorCss = models.CharField(max_length=50, default='', blank=True, editable=False)


	def get_absolute_url(self):		
		kwargs = {
			'year': self.timestamp.year,
			'month': self.timestamp.month,
			'day': self.timestamp.day,
			'pk': self.pk,
			'slug': self.slug
        }
		return reverse('post_detail', kwargs=kwargs)

	def get_preview_post(self):
		lista = list(Post.objects.filter(state='p'))
		previewIndex = lista.index(self)-1
		previewPost = None if previewIndex < 0 else lista[previewIndex]
		return previewPost

	def get_next_post(self):
		lista = list(Post.objects.filter(state='p'))
		nextIndex = lista.index(self)+1
		nextPost = None if nextIndex >= len(lista) else lista[nextIndex]
		return nextPost


	def __str__(self):
		return self.title



@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
	colors = ['purple','orange','navy','red','lime','green','blue']
	lastPost = Post.objects.last()
	if lastPost == None:
		instance.colorCss = colors[0]
	elif instance.slug ==  None or instance.slug == '':
		colorLastIndex = colors.index(lastPost.colorCss)
		if (colorLastIndex + 1) < len(colors):
			instance.colorCss = colors[colorLastIndex + 1]
		else:
			instance.colorCss = colors[0]

	instance.slug = slugify(instance.title)