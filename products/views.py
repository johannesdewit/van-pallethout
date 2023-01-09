from django.views import generic
from .models import Product, Model

# Create your views here.

# IndexViews
class IndexView(generic.ListView):
    template_name = 'products/index.html'

    def get_queryset(self):
        """Return published items."""
        return self.model.objects.filter(visibility_status='p')

class ProductIndexView(IndexView):
    model = Product
    context_object_name = 'products'

class ModelIndexView(IndexView):
    model = Model
    template_name = 'products/model-index.html'
    context_object_name = 'models'


# DetailViews
class DetailView(generic.DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'item'

    def get_queryset(self):
        return self.model.objects.filter(visibility_status='p')

class ProductDetailView(DetailView):
    model = Product

class ModelDetailView(DetailView):
    model = Model
