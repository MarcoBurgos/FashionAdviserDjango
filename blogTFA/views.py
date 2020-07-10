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
        posts = Post.objects.filter(status='PUBLISHED')
        context['posts'] = posts
        print(len(posts))
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
