from django.urls import path

from .views import IndexTemplateView

app_name = 'blog'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
]