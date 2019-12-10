from django.urls import path
from . import views

app_name = 'empresas'
urlpatterns = [
    # ex: /empresas/
    path('', views.index, name='index'),
]