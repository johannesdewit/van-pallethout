from django.views import generic
from .models import Album

# Create your views here.
class AlbumIndexView(generic.ListView):
    template_name = "album/index.html"
    model = Album
    context_object_name = "albums"

    def get_queryset(self):
        """Return published items."""
        return self.model.objects.filter(visibility_status="p")
