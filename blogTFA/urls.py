from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView, PostDetailView, CategoryView

urlpatterns = [
    # path('', views.index, name="index"),
    path('', IndexView.as_view(extra_context={"instagram_profile_name": "the.fashion.adviser"}), name="index"),
    path('<str:category>/', CategoryView.as_view(extra_context={"instagram_profile_name": "the.fashion.adviser"}), name='category'),
    path('<str:category>/<slug:slug>/', PostDetailView.as_view(extra_context={"instagram_profile_name": "the.fashion.adviser"}), name='post-detail'),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
