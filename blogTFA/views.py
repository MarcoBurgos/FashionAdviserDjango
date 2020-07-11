from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.db.models import Count

# def index(request):
#     return render(request, 'index.html', {})

count = Post.objects.all().values('category_name').annotate(total=Count('category_name')).order_by('-total')
counts = dict()
for item in count:
    counts[item['category_name']] = item['total']

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(status='PUBLISHED')
        context['posts'] = posts
        context['count'] = counts
        return context

class CategoryView(ListView):
    model = Post
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = counts
        return context




    def get_context_data(self, **kwargs):
        category= self.kwargs['category'].capitalize()
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(status='PUBLISHED', category_name=category)
        context['posts'] = posts
        context['category'] = category
        context['count'] = counts
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
