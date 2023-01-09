from django_extensions.db.fields import AutoSlugField
from django.db import models


VISIBILITY_STATUS_OPTIONS = {
        ('a', "archived"),
        ('d', "draft"),
        ('p', "published")
    }

class CommonInfo(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField(null=True)
    visibility_status = models.CharField(choices=VISIBILITY_STATUS_OPTIONS, max_length=1, null=False, default="draft")

    class Meta:
        abstract = True

class Product(CommonInfo):
    model = models.ForeignKey('Model', on_delete=models.CASCADE, null=True)

class Model(CommonInfo):
    pass

