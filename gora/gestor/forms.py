from django.forms import ModelForm
from .models import Delivery, Order

class DeliveryForm(ModelForm):
    class Meta: 
        model = Delivery
        fields = ['name', 'last_name', 'phone', 'cart_size']

class OrderForm(ModelForm):
    class Meta: 
        model = Order
        fields = ['name', 'address', 'qty', 'is_forever', 'observations', 'order_type', 'order_shift', 
    'delivery_assigned', 'date', 'state']