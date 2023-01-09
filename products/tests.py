from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from .models import Product


def create_product(product_name, product_description, product_visibility):
    """
    Create a product.
    """
    return Product.objects.create(
        name=product_name,
        description=product_description,
        visibility_status=product_visibility,
        )


class ProductIndexViewTests(TestCase):
    def test_no_products(self):
        """
        If no products exist, a message is displayed
        """
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Geen producten beschikbaar.")
        self.assertQuerysetEqual(response.context['products'], [])

    def test_products(self):
        """
        Only published products show up in the index
        """
        product_pub = create_product(
            product_name="Test product published",
            product_description="Test beschrijving",
            product_visibility="p"
        )

        product_arch = create_product(
            product_name="Test product archived",
            product_description="Test beschrijving",
            product_visibility="a"
        )

        product_draft = create_product(
            product_name="Test product draft",
            product_description="Test beschrijving",
            product_visibility="d"
        )

        response = self.client.get(reverse('products:index'))
        self.assertQuerysetEqual(
            response.context['products'],
            [product_pub],
        )

class ProductDetailViewTests(TestCase):
    product_name = "Test product"
    product_description="Test beschrijving"

    def test_published_product(self):
        """
        The detail view of a published product is accessible and
        shows the description.
        """
        product_pub = create_product(
            self.product_name,
            self.product_description,
            product_visibility="p"
        )
        url = reverse('products:detail', args=(product_pub.slug,))
        response = self.client.get(url)
        self.assertContains(response, product_pub.description)
    
    def test_archived_product(self):
        """
        The detail view of a archived product returns a 404 not
        found.
        """
        product_arch = create_product(
            product_name="Test product archived",
            product_description="Test beschrijving",
            product_visibility="a"
        )
        url = reverse('products:detail', args=(product_arch.slug,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_draft_product(self):
        """
        The detail view of a draft product returns a 404 not
        found.
        """
        product_draft = create_product(
            product_name="Test product draft",
            product_description="Test beschrijving",
            product_visibility="d"
        )
        url = reverse('products:detail', args=(product_draft.slug,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

# TODO: Write test for Model Class