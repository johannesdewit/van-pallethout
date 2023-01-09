from django_extensions.db.fields import AutoSlugField
from django.db import models

from .validators import validate_hex_code


VISIBILITY_STATUS_OPTIONS = {
        ('a', "archived"),
        ('d', "draft"),
        ('p', "published")
    }

class CommonInfo(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField(null=True)
    visibility_status = models.CharField(
        choices=VISIBILITY_STATUS_OPTIONS,
        max_length=1,
        null=False, 
        default="draft"
    )

    class Meta:
        abstract = True

class Product(CommonInfo):
    model = models.ForeignKey('Model', on_delete=models.CASCADE, null=True)
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)

class Model(CommonInfo):
    type = models.ForeignKey('Type', on_delete=models.CASCADE, null=True)
    dimensions = models.CharField(
        max_length=40,
        null=False,
        help_text="Please use the following format: <em>Width x Length x Height</em>."
    )

class Type(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

class Color(models.Model):
    name = models.CharField(max_length=120, unique=True)
    hex_code = models.CharField(
        unique=True,
        null=False,
        validators=[validate_hex_code] 
    )
    paint_type = models.CharField(max_length=60, null=True)




