import random

from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError

from .models import Color, Product, Model


def create_product(product_name, product_description, product_visibility):
    """
    Create a product.
    """
    return Product.objects.create(
        name=product_name,
        description=product_description,
        visibility_status=product_visibility,
    )


def create_model(model_name, model_description, model_visibility):
    """
    Create a model.
    """
    return Model.objects.create(
        name=model_name,
        description=model_description,
        visibility_status=model_visibility,
    )


# MODEL TESTS
class ColorTests(TestCase):
    def setUp(self):
        self.valid_color = Color.objects.create(
            name="valid color",
            hex_code="#000000",
            paint_type="lijnolie"
        )

    def test_hex_code_validation(self):
        """
        Only Color objects with valid hex codes are created.
        """

        non_valid_codes = [
            str(random.randrange(1, 999999)),
            "#" + str(random.randrange(1, 99)),
            "#" + str(random.randrange(1000000, 9999999)),
            "#FFFFFN",
        ]
        for code in non_valid_codes:
            with self.assertRaises(ValidationError):
                Color.objects.create(
                    name="non valid color", hex_code=code, paint_type="lijnolie"
                )

        self.assertEqual(Color.objects.all().get(), self.valid_color)

class ProductTests(TestCase):
    def setUp(self):
        self.model = Model.objects.create(
            name="model",
            visibility_status="p",
            dimensions="w x l x h"
        )
        self.product = Product.objects.create(
            name="product",
            visibility_status="p",
            model=Model.objects.get(name="model")
        )

    def test_product_dimensions(self):
        self.assertEqual(Model.objects.get(name="model").dimensions, Product.objects.get(name="product").model.dimensions)


# VIEW TESTS
# IndexView Tests
class ProductIndexViewTests(TestCase):
    def test_no_products(self):
        """
        If no products exist, a message is displayed
        """
        response = self.client.get(reverse("products:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Geen producten beschikbaar.")
        self.assertQuerysetEqual(response.context["products"], [])

    def test_products(self):
        """
        Only published products show up in the index
        """
        product_pub = create_product(
            product_name="Test product published",
            product_description="Test beschrijving",
            product_visibility="p",
        )

        product_arch = create_product(
            product_name="Test product archived",
            product_description="Test beschrijving",
            product_visibility="a",
        )

        product_draft = create_product(
            product_name="Test product draft",
            product_description="Test beschrijving",
            product_visibility="d",
        )

        response = self.client.get(reverse("products:index"))
        self.assertQuerysetEqual(
            response.context["products"],
            [product_pub],
        )


class ModelIndexViewTests(TestCase):
    def test_no_models(self):
        """
        If no models exist, a message is displayed
        """
        response = self.client.get(reverse("products:model-index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Geen modellen beschikbaar.")
        self.assertQuerysetEqual(response.context["models"], [])

    def test_models(self):
        """
        Only published models show up in the index
        """
        model_pub = create_model(
            model_name="Test model published",
            model_description="Test beschrijving",
            model_visibility="p",
        )

        model_arch = create_model(
            model_name="Test model archived",
            model_description="Test beschrijving",
            model_visibility="a",
        )

        model_draft = create_model(
            model_name="Test model draft",
            model_description="Test beschrijving",
            model_visibility="d",
        )

        response = self.client.get(reverse("products:model-index"))
        self.assertQuerysetEqual(
            response.context["models"],
            [model_pub],
        )


# DetailView Tests
class ProductDetailViewTests(TestCase):
    product_name = "Test product"
    product_description = "Test beschrijving"

    def test_published_product(self):
        """
        The detail view of a published product is accessible and
        shows the description.
        """
        product_pub = create_product(
            self.product_name, self.product_description, product_visibility="p"
        )
        url = reverse("products:detail", args=(product_pub.slug,))
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
            product_visibility="a",
        )
        url = reverse("products:detail", args=(product_arch.slug,))
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
            product_visibility="d",
        )
        url = reverse("products:detail", args=(product_draft.slug,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class ModelDetailViewTests(TestCase):
    model_name = "Test model"
    model_description = "Test beschrijving"

    def test_published_model(self):
        """
        The detail view of a published model is accessible and
        shows the description.
        """
        model_pub = create_model(
            self.model_name, self.model_description, model_visibility="p"
        )
        url = reverse("products:model-detail", args=(model_pub.slug,))
        response = self.client.get(url)
        self.assertContains(response, model_pub.description)

    def test_archived_product(self):
        """
        The detail view of a archived model returns a 404 not
        found.
        """
        model_arch = create_model(
            model_name="Test model archived",
            model_description="Test beschrijving",
            model_visibility="a",
        )
        url = reverse("products:model-detail", args=(model_arch.slug,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_draft_model(self):
        """
        The detail view of a draft model returns a 404 not
        found.
        """
        model_draft = create_model(
            model_name="Test model draft",
            model_description="Test beschrijving",
            model_visibility="d",
        )
        url = reverse("products:model-detail", args=(model_draft.slug,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
