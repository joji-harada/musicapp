from django.contrib import admin
from .models import MusicType, Product, Review

# Register your models here.
admin.site.register(MusicType)
admin.site.register(Product)
admin.site.register(Review)