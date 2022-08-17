
 from django.db import models

# Create your models here.
def Album(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    creation_date = models.DateField(auto_now_add=True)

    # Should be prepopulated according to title! See: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields
    slug = models.SlugField()

    # Default place to safe thumbnails should be specified! https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.FileField.upload_to
    thumbnail = models.ImageField()

    class Meta:
        ordering = ['-creation_date', 'title']
        unique_together = ['creation_date', 'title']

    # Should be addressed later on according to https://docs.djangoproject.com/en/4.0/ref/models/instances/#get-absolute-url
    def get_absolute_url(self):
