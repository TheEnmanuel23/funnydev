from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from  .models import *

# Create your views here.
class PostList( ListView ):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get (self, request, *args, **kwargs):
        self.object_list = self.model.objects.filter(state = 'p')
        valueToFind = request.GET.get('value')

        if valueToFind:
            self.object_list = self.model.objects.filter(
                Q(title__icontains=valueToFind) |
                Q(content__icontains=valueToFind) |
                Q(author__name__icontains=valueToFind) |
                Q(category__nombre__icontains=valueToFind)
            ).distinct()
        return self.render_to_response(self.get_context_data())

class PostDetail( DetailView ):
    model = Post
    template_name = 'post_detail.html'