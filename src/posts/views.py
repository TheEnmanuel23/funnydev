from django.shortcuts import render
from django.views.generic import ListView, DetailView
from  .models import *

# Create your views here.
class PostList( ListView ):
    model = Post
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
    	context = super(PostList, self).get_context_data(**kwargs)
    	context["posts"] = Post.objects.filter(state = 'p')
    	return context

class PostDetail( DetailView ):
	model = Post
	template_name = 'post_detail.html'