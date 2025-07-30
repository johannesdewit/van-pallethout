from django_extensions.db.fields import AutoSlugField

from django.conf import settings
from django.db import models

from .validators import validate_hex_code


VISIBILITY_STATUS_OPTIONS = {("a", "archived"), ("d", "draft"), ("p", "published")}
AVAILABILITY_STATUS_OPTIONS = {
    ("a", "available"),
    ("so", "sold out"),
    ("r", "on request"),
}


class CommonInfo(models.Model):
    """
    Contains information required by Products and Models.
    """

    name = models.CharField("Name", max_length=120, unique=True, blank=False)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField("Descriptions", blank=True, null=True)
    visibility_status = models.CharField(
        choices=VISIBILITY_STATUS_OPTIONS, max_length=1, blank=False, default="d"
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
    colors = models.ManyToManyField("Color", blank=True)
    material = models.ManyToManyField("Material", blank=True)

    # Shop info
    available = models.CharField(
        max_length=2, choices=AVAILABILITY_STATUS_OPTIONS, blank=False, default="a"
    )
    available_from = models.DateField(null=True, blank=True)
    stock = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default="0")

    # TODO: Images
    thumbnail = models.ImageField(
        upload_to='images/thumbnails', null=True, blank=True
    )
    image_folder = models.FilePathField(
        path=settings.IMAGES_PATH,
        allow_files=False,
        allow_folders=True,
        blank=True,
        null=True,
    )

    def properties(self):
        return [
            self.model,
            self.colors,
            self.material,
        ]


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
    dimensions_seat = models.CharField(
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

    name = models.CharField("Model name", max_length=120, unique=True, blank=False)
    hex_code = models.CharField(
        "Color hex code",
        max_length=7,
        unique=True,
        blank=False,
        validators=[validate_hex_code],
    )
    paint_type = models.CharField(max_length=60, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Material(models.Model):
    """
    Material model which contains possible materials for products.
    """

    name = models.CharField("Material name", max_length=120, unique=True, blank=False)

    def __str__(self):
        return self.name
