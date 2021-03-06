from django.contrib import admin
from .models import *

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title','timestamp','updated',]
	list_display_links = ['updated',]
	list_editable = ['title',]
	list_filter = ['updated','timestamp','state']
	search_fields = ['title', 'content']

	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Author)