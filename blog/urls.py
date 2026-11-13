from django.urls import path

from .views import IndexTemplateView, ArtikelListView, ArtikelDetailView

app_name = 'blog'

urlpatterns = [
    path('artikel/<int:pk>/', ArtikelDetailView.as_view(), name='detail'),
    path('artikel/', ArtikelListView.as_view(), name='artikel'),
    path('', IndexTemplateView.as_view(), name='index'),
]