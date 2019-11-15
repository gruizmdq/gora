from django.contrib import admin
from .models import Delivery, Order

admin.site.register([Delivery, Order])