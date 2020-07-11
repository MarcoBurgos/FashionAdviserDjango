from django.urls import path
#from. import views
from .views import IndexView, PostDetailView, CategoryView

urlpatterns = [
    # path('', views.index, name="index"),
    path('', IndexView.as_view(), name="index"),
    path('category/<str:category>/', CategoryView.as_view(), name='category'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
