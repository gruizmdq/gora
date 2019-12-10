import django
from django.db import models
from django.conf import settings
from datetime import date

class Empresa(models.Model):
    name = models.CharField(max_length=50, default="", verbose_name=u"Nombre")
    phone = models.CharField(max_length=15, default="", verbose_name=u"Teléfono")
    address = models.CharField(max_length=50, default="", verbose_name=u"Dirección")

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50, default="", verbose_name=u"Nombre")
    is_forever = models.BooleanField(default=False, verbose_name=u"Es un menú fijo?")
    date = models.DateTimeField(
        default=django.utils.timezone.now, 
        verbose_name=u"Fecha del pedido" 
    )
    def __str__(self):
        return self.name

class Order(models.Model):
    id_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.SET_NULL,
        verbose_name="Empresa:",
        null=True
    )
    id_empleado = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    id_menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        verbose_name="Menú:",
        null=True
    )
    date = models.DateField(
        default=date.today, 
        verbose_name=u"Fecha del menú" 
    )
    
    def __str__(self):
        return self.id_empleado.name + " " + self.id_empresa.name + " " + self.id_menu.name + " " + self.date.strftime('%H:%M - %Y/%m/%d')
