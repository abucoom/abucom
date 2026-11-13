from django.db import models
from django.utils.text import slugify

class Penulis(models.Model):
    nama   = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id}. {self.nama}"

class Kategori(models.Model):
    nama       = models.CharField(max_length=255)
    keterangan = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id}. {self.nama}"

class Artikel(models.Model):
    judul      = models.CharField(max_length=255)
    isi        = models.TextField()
    kategori   = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    penulis    = models.ForeignKey(Penulis, on_delete=models.CASCADE)
    publish    = models.BooleanField(default=False)
    views      = models.IntegerField(default=0, editable=False)
    slug       = models.SlugField(unique=True, blank=True, editable=False)
    created    = models.DateTimeField(auto_now_add=True, editable=False)
    updated    = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.CharField(max_length=255, blank=True, editable=False)
    updated_by = models.CharField(max_length=255, blank=True, editable=False)

    def __str__(self):
        return f"{self.id}. {self.judul}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

class Komentar(models.Model):
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    pesan   = models.TextField()
    oleh    = models.CharField(max_length=255, blank=True, editable=False)

    def __str__(self):
        return f"{self.id}. {self.pesan}"