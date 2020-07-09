from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def index(request):
#     return render(request, 'index.html', {})

class IndexView(ListView):
    model = Post
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_posts'] = Post.objects.filter(status='Published')[0:4]
        context['feature_posts'] = Post.objects.filter(status='Published')[4:6]
        return context
