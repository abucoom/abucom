from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    template_name = "blog/index.html"
    extra_context = {"page_title": "blog"}