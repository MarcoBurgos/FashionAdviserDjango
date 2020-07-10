from django.urls import path
#from. import views
from .views import IndexView, PostDetailView

urlpatterns = [
    # path('', views.index, name="index"),
    path('', IndexView.as_view(), name="index"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
