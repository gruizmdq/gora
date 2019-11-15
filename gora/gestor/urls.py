from django.urls import path
from . import views

urlpatterns = [
    # ex: /gestor/
    path('', views.index, name='index'),
    # ex: /gestor/orders/5/
    path('orders/<int:id>/', views.order_detail, name='order_detail'),
    # ex: /gestor/orders/add/
    path('orders/add/', views.order_add, name='order_add'),
    # ex: /gestor/delivery/
    path('delivery/', views.delivery, name='delivery'),
    # ex: /gestor/delivery/id
    path('delivery/<int:id>/', views.delivery_detail, name='delivery_detail'),
    # ex: /gestor/delivery/add
    path('delivery/add/', views.delivery_add, name='delivery_add'),
]