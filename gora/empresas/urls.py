from django.urls import path
from . import views

app_name = 'empresas'
urlpatterns = [
    # ex: /empresas/
    path('', views.index, name='index'),
    path('order_add/', views.order_add, name='order_add'),
]