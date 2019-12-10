from django.forms import ModelForm
from django import forms
from django.db.models import Q
from .models import Order, Menu

class OrderForm(ModelForm):
    #id_menu = forms.ModelChoiceField(queryset=Menu.objects.filter(is_forever = True).all(), empty_label="(Nothing)")
    
    def __init__(self, *args, **kwargs):
        date = kwargs.get('initial').get('date')
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['id_menu'] = forms.ModelMultipleChoiceField(
                required=True,
                queryset=Menu.objects.filter(Q(date__contains=date) | Q(is_forever=True)).all(),
               )
    
    class Meta: 
        model = Order
        fields = ['id_menu', 'date']
        widgets = {'id_menu': forms.RadioSelect}
    