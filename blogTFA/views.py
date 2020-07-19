from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import Post, Subscribers
from . import forms
from django.db.models import Count
import pprint
import json, re, requests

def get_count():
    try:
        count = Post.objects.all().filter(status='PUBLISHED').values('category_name').annotate(total=Count('category_name')).order_by('-total')
        counts = dict()
        for item in count:
            counts[item['category_name']] = item['total']
    except Exception as e:
        print(f"there was an error {e}")
    return counts


def fetch_media():
    user = 'the.fashion.adviser'
    profile = 'https://www.instagram.com/' + user
    photos_from_instagram = []

    with requests.session() as s:
        s.headers['user-agent'] = 'Mozilla/5.0'

        end_cursor = ''
        for count in range(1, 2):
            print('PAGE: ', count)

            r    = s.get(profile, params={'max_id': end_cursor})
            data = re.search(
                r'window._sharedData = (\{.+?});</script>', r.text).group(1)

            j = json.loads(data)

            try:
                media = j['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

                for node in media:
                    values = dict()
                    values['display_url'] = node['node']['display_url']
                    values['shortcode'] = node['node']['shortcode']
                    photos_from_instagram.append(values)
            except Exception as e:
                f = open("logs.txt", "w")
                f.write(data)
                f.close()


    return photos_from_instagram


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6
    queryset = Post.objects.filter(status='PUBLISHED')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = get_count()
        context['photos'] = fetch_media()
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
        context['photos'] = fetch_media()
        context['count'] = get_count()
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
        context['photos'] = fetch_media()
        context['count'] = get_count()
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
