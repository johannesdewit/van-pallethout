from django.db import models

from django_extensions.db.fields import AutoSlugField

from vanpallethout.constants import VISIBILITY_STATUS_OPTIONS


class Album(models.Model):
    name = models.CharField(max_length=60)
    slug = AutoSlugField(populate_from="name", unique=True)
    visibility_status = models.CharField(
        choices=VISIBILITY_STATUS_OPTIONS, max_length=1, blank=False, default="d"
    )

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(
        upload_to='images/', null=False, blank=False
    )
    slug = AutoSlugField(populate_from="name", unique=True)
    visibility_status = models.CharField(
        choices=VISIBILITY_STATUS_OPTIONS, max_length=1, blank=False, default="d"
    )
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    albums = models.ManyToManyField(Album, blank=True)


    def __str__(self):
        return self.name