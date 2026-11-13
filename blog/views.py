from django.views.generic import TemplateView, ListView

from .models import Artikel

class ArtikelListView(ListView):
    model = Artikel
    extra_context = {"page_title": "artikel"}

class IndexTemplateView(TemplateView):
    template_name = "blog/index.html"
    extra_context = {"page_title": "blog"}