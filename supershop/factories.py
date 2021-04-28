import factory
from factory.django import DjangoModelFactory

from .models import Product, Order, OrderProduct


# Defining a factory
class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    # See the list of factory providers at
    # https://faker.readthedocs.io/en/stable/providers.html
    name = factory.Faker("company")
    description = factory.Faker(
        "sentence",
        nb_words=128,
        variable_nb_words=True
    )


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    customer_name = factory.Faker("name")
    customer_address = factory.Faker("address")
    creation_date = factory.Faker("date")


class OrderProductFactory(DjangoModelFactory):
    class Meta:
        model = OrderProduct
