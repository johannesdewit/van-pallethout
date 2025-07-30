from django.contrib import admin

from .models import Color, Product, Material, Model, Type

# Register your models here.
admin.site.register(Product)
admin.site.register(Model)
admin.site.register(Type)
admin.site.register(Material)
admin.site.register(Color)