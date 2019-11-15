import django
from django.db import models
class Delivery(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cart_size = models.IntegerField(default=0)
    orders_shipped = models.IntegerField(default=0)
    orders_failure = models.IntegerField(default=0)

class Order(models.Model):
    ORDER_TYPE = (
        ('S', 'Salad'),
        ('B', 'Balance'),
        ('T', 'Temping')
    )
    ORDER_TIME = (
        ('H1', 'Turno 1'),
        ('H2', 'Turno 2')
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    qty = models.IntegerField(default=1)
    observations = models.TextField(verbose_name=u"Observaciones")
    order_type = models.CharField(
        max_length = 1,
        choices = ORDER_TYPE
    )
    order_time = models.CharField(
        max_length = 2,
        choices = ORDER_TIME
    )