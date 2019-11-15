import django
from django.db import models
from datetime import datetime, timedelta

class Delivery(models.Model):
    name = models.CharField(max_length=50, default="", verbose_name=u"Nombre")
    last_name = models.CharField(max_length=50, default="", verbose_name=u"Apellido")
    phone = models.CharField(max_length=15, default="", verbose_name=u"Celular")
    cart_size = models.IntegerField(default=0, verbose_name=u"Pedidos que puede llevar")
    orders_shipped = models.IntegerField(default=0)
    orders_failure = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + self.last_name

class Order(models.Model):
    ORDER_SHIFT = (
        ('H1', 'Turno 1'),
        ('H2', 'Turno 2')
    )
    ORDER_STATE = (
        ('B', 'Blanco'),
        ('En', 'Entregado'),
        ('Ca', 'Cancelado'),
        ('Ve', 'Verde'),
        ('R', 'Rojo'),
        ('Az', 'Azul'),
        ('Ro', 'Rosa'),
        ('Am', 'Amarillo')
    )
    name = models.CharField(max_length=50, default="", verbose_name=u"Nombre")
    address = models.CharField(max_length=150, default="", verbose_name=u"Dirección")
    qty = models.IntegerField(default=1, verbose_name=u"Cantidad")
    is_forever = models.BooleanField(default=False, verbose_name=u"Es un pedido fijo?")
    observations = models.TextField(verbose_name=u"Observaciones", null=True)    
    order_shift = models.CharField(
        max_length = 2,
        verbose_name=u"Turno",
        choices = ORDER_SHIFT
    )
    delivery_assigned = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        verbose_name="Delivery:",
        null=True
    )
    date = models.DateTimeField(
        default=django.utils.timezone.now, 
        verbose_name=u"Fecha del pedido", 
        help_text=u"MODIFICAR SOLAMENTE EN CASO DE NO SER PARA EL DÍA DE LA FECHA"
    )
    state = models.CharField(
        max_length = 2,
        verbose_name=u"Estado",
        choices = ORDER_STATE,
        default = "B"
    )

class Order_Item(models.Model):
    ORDER_TYPE = (
        ('S', 'Salad'),
        ('B', 'Balance'),
        ('T', 'Temping')
    )
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1, verbose_name=u"Cantidad")
    order_type = models.CharField(
        max_length = 1,
        choices = ORDER_TYPE
    )
