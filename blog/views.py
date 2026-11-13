from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Artikel

class ArtikelCreateView(CreateView):
    model  = Artikel
    fields = ("judul", "isi", "kategori", "penulis", "publish",)
    success_url = reverse_lazy("blog:index")

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