from django_extensions.db.fields import AutoSlugField
from django.db import models

from .validators import validate_hex_code


VISIBILITY_STATUS_OPTIONS = {("a", "archived"), ("d", "draft"), ("p", "published")}


class CommonInfo(models.Model):
    """
    Contains information required by Products and Models.
    """

    name = models.CharField(max_length=120, unique=True, blank=False)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField(blank=True, null=True)
    visibility_status = models.CharField(
        choices=VISIBILITY_STATUS_OPTIONS, max_length=1, blank=False, default="draft"
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Product(CommonInfo):
    """
    Product model
    """

    model = models.ForeignKey("Model", on_delete=models.CASCADE, blank=True, null=True)
    colors = models.ManyToManyField("Color")


class Model(CommonInfo):
    """
    Model model
    """

    type = models.ForeignKey("Type", on_delete=models.CASCADE, blank=True, null=True)
    dimensions = models.CharField(
        max_length=40,
        help_text="Please use the following format: <em>Width x Length x Height</em>.",
        blank=True,
        null=True,
    )


class Type(models.Model):
    """
    Type of furniture model
    """

    name = models.CharField(max_length=120, unique=True, blank=False)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    """
    Color model which contains possible colors for products.
    """

    name = models.CharField(max_length=120, unique=True, blank=False)
    hex_code = models.CharField(
        max_length=7, unique=True, blank=False, validators=[validate_hex_code]
    )
    paint_type = models.CharField(max_length=60, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
