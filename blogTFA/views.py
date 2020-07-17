from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import Post, Subscribers
from . import forms
from django.db.models import Count
import pprint


try:
    count = Post.objects.all().filter(status='PUBLISHED').values('category_name').annotate(total=Count('category_name')).order_by('-total')
    counts = dict()
    for item in count:
        counts[item['category_name']] = item['total']
except Exception as e:
    print(f"there was an error {e}") 


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6
    queryset = Post.objects.filter(status='PUBLISHED')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = counts
        email_form = forms.EmailForm()
        context['email_form']= email_form
        del context['post_list']
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(context)
        return context

class CategoryView(ListView):
    model = Post
    template_name = 'category.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category= self.kwargs['category'].capitalize()
        context['category'] = category
        context['count'] = counts
        email_form = forms.EmailForm()
        context['email_form']= email_form

        posts = Post.objects.filter(status='PUBLISHED', category_name=category)
        paginator = Paginator(posts, per_page=4)
        page = self.request.GET.get('page')

        try:
            posts_pg = paginator.page(page)
        except PageNotAnInteger:
            posts_pg = paginator.page(1)
        except EmptyPage:
            posts_pg = paginator.page(paginator.num_pages)

        context['page_obj'] = posts_pg
        context['paginator'] = paginator
        context['is_paginated'] = True
        context['object_list'] = posts

        del context['post_list']
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(context)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        post = Post.objects.filter(slug__iexact=slug)
        if post[0].carousel_urls:
            urls = post[0].carousel_urls.split(",")
            context['urls'] = urls

        context['post'] = post
        context['count'] = counts
        email_form = forms.EmailForm()
        context['email_form']= email_form
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(context)
        return context


def ajax_call(request):
    print(f"inside ajax call")
    if request.method == 'GET':
        email = request.GET.get('email', None)
        data = {
             'is_there': Subscribers.objects.filter(email__exact=email).exists()
         }
        if data['is_there']:
            data['error_message'] = 'El correo ya está registrado'

        else:
            record = Subscribers(email=email)
            record.save()
            data['success_message'] = 'Mail agregado.'


        print(str(data))

        return JsonResponse(data)
