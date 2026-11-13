from django.urls import path

from .views import (
    IndexTemplateView, ArtikelListView, ArtikelDetailView, ArtikelCreateView, 
    ArtikelUpdateView,
)

app_name = 'blog'

urlpatterns = [
    path('update/<int:pk>/', ArtikelUpdateView.as_view(), name='update'),
    path('create/', ArtikelCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ArtikelDetailView.as_view(), name='detail'),
    path('artikel/', ArtikelListView.as_view(), name='artikel'),
    path('', IndexTemplateView.as_view(), name='index'),
]