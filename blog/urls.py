from django.urls import path

from .views import IndexTemplateView, ArtikelListView

app_name = 'blog'

urlpatterns = [
    path('artikel/', ArtikelListView.as_view(), name='artikel'),
    path('', IndexTemplateView.as_view(), name='index'),
]