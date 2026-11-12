from django.contrib import admin

from .models import Artikel, Kategori, Penulis, Komentar

class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = (
        "views",
        "slug", 
        "created", 
        "updated",
        "created_by",
        "updated_by",
    )

class KomentarAdmin(admin.ModelAdmin):
    readonly_fields = ("oleh",)

admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Kategori)
admin.site.register(Penulis)
admin.site.register(Komentar, KomentarAdmin)