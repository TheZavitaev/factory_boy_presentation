from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)

    class Meta:
        verbose_name = _('продукт')
        verbose_name_plural = _('продукты')

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    customer_name = models.CharField(_('имя заказчика'), max_length=255)
    customer_address = models.TextField(_('адрес заказчика'), blank=False)
    creation_date = models.DateField(_('дата создания заказа'), blank=True)

    class Meta:
        verbose_name = _('заказ')
        verbose_name_plural = _('заказы')

    def __str__(self):
        return self.customer_name 


class OrderProduct(models.Model):
    quantity = models.IntegerField(_('количество'), null=False) 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
