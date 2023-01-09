from django.views import generic
from .models import Product, Model

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Return published products."""
        return Product.objects.filter(visibility_status='p')

class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_queryset(self):
        return self.model.objects.filter(visibility_status='p')

class ModelIndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        """Return published products of the model."""
        return Model.objects.filter(visibility_status='p')

class ModelDetailView(DetailView):
    model = Model
