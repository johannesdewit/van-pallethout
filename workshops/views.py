from django.views import generic
from .models import Workshop

# Create your views here.
# IndexViews
class IndexView(generic.ListView):
    template_name = "workshops/index.html"

    def get_queryset(self):
        """Return published items."""
        return self.model.objects.filter(visibility_status="p")
    
class WorkshopIndexView(IndexView):
    model = Workshop
    context_object_name = "workshops"

# DetailViews
class DetailView(generic.DetailView):
    template_name = "workshop/detail.html"
    context_object_name = "item"

    def get_queryset(self):
        return self.model.objects.filter(visibility_status="p")
    
class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = "workshop/workshop-detail.html"