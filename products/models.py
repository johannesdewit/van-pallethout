from django_extensions.db.fields import AutoSlugField
from django.db import models


VISIBILITY_STATUS_OPTIONS = {
        ('a', "archived"),
        ('d', "draft"),
        ('p', "published")
    }

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField(null=True)
    visibility_status = models.CharField(choices=VISIBILITY_STATUS_OPTIONS, max_length=1, null=False, default="draft")
    model = models.ForeignKey(Model, on_delete=SET_NULL, null=True)

class Model(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField(null=True)
    visibility_status = models.CharField(choices=VISIBILITY_STATUS_OPTIONS, max_length=1, null=False, default="draft")

