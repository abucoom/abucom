from django.urls import path

from .views import IndexTemplateView, ArtikelListView, ArtikelDetailView, ArtikelCreateView

app_name = 'blog'

urlpatterns = [
    path('create/', ArtikelCreateView.as_view(), name='create'),
    path('artikel/<int:pk>/', ArtikelDetailView.as_view(), name='detail'),
    path('artikel/', ArtikelListView.as_view(), name='artikel'),
    path('', IndexTemplateView.as_view(), name='index'),
]