from django.forms import ModelForm
from django import forms
from .models import Delivery, Order, Order_Item

class DeliveryForm(ModelForm):
    class Meta: 
        model = Delivery
        fields = ['name', 'last_name', 'phone', 'cart_size']

class OrderForm(ModelForm):
    class Meta: 
        model = Order
        fields = ['name', 'address', 'is_forever', 'observations', 'order_shift', 
    'delivery_assigned', 'date', 'state']

class TypeOrderForm(ModelForm):
    class Meta: 
        model = Order_Item
        fields = ['id_order', 'qty', 'order_type']