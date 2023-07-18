from django_extensions.db.fields import AutoSlugField

from django.db import models

VISIBILITY_STATUS_OPTIONS = {("a", "archived"), ("d", "draft"), ("p", "published")}

# Create your models here.
class Workshop(models.Model):
    """
    Workshop model
    """
    
    name = models.CharField("Name", max_length=120, unique=True, blank=False)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField("Descriptions", blank=True, null=True)
    preview_text = models.TextField(max_length=180, blank=True, null=True)
    visibility_status = models.CharField(
        choices=VISIBILITY_STATUS_OPTIONS, max_length=1, blank=False, default="d"
    )
    available_from = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default="0")
    minimum_participants = models.PositiveSmallIntegerField(default=2)
    maximum_participants = models.PositiveSmallIntegerField(default=16)

    # TODO: Images

    def __str__(self):
        return self.name