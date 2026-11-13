from django.views.generic import TemplateView, ListView, DetailView

from .models import Artikel

class ArtikelDetailView(DetailView):
    model = Artikel
    extra_context = {"page_title": "detail"}

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=["views"])
        return obj

class ArtikelListView(ListView):
    model = Artikel
    extra_context = {"page_title": "artikel"}

class IndexTemplateView(TemplateView):
    template_name = "blog/index.html"
    extra_context = {"page_title": "blog"}