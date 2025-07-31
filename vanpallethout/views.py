from django.views import generic
from workshops.models import Workshop

# Create your views here.
# IndexViews
class IndexView(generic.ListView):
    template_name = "index.html"
    model = Workshop
    context_object_name = "workshops"

    def get_queryset(self):
        """Return published items."""
        return self.model.objects.filter(visibility_status="p")