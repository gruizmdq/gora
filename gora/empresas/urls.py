from django.urls import path
from . import views

app_name = 'empresas'
urlpatterns = [
    # ex: /empresas/
    path('', views.index, name='index'),
    path('add_orders/', views.add_orders, name='add_orders'),
]