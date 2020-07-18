from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView, PostDetailView, CategoryView, ajax_call
from blogTFA import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', IndexView.as_view(), name="index"),
    path('<str:category>/', CategoryView.as_view(), name='category'),
    path('<str:category>/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('summernote/', include('django_summernote.urls')),
    path('callback/forms/ajax_call/', views.ajax_call, name='ajax_call'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
