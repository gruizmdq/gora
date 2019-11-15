from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from .models import Order, Delivery
from .forms import *


def index(request):
    today_orders = Order.objects.filter(date__contains = today()).order_by('-date') 
    context = {'orders': today_orders}
    return render(request, 'index.html', context)



#### ORDERS #############

def order_detail(request, id):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('order_detail', id=post.pk)
    else:
        try:
            delivery = Delivery.objects.get(pk=id)
        except Delivery.DoesNotExist:
            raise Http404("Question does not exist")
    form = DeliveryForm(instance=delivery)
    return render(request, 'order_detail.html', {'form': form})

def order_add(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('order_detail', id=post.pk)
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'order_add.html', context)


##### DELIVERY ##########
def delivery(request):
    deliverys = Delivery.objects.all()
    context = {'deliverys': deliverys}
    return render(request, 'delivery.html', context)

def delivery_detail(request, id):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('delivery_detail', id=post.pk)
    else:
        try:
            delivery = Delivery.objects.get(pk=id)
        except Delivery.DoesNotExist:
            raise Http404("Question does not exist")
    form = DeliveryForm(instance=delivery)
    return render(request, 'delivery_detail.html', {'form': form})

def delivery_edit(request, id):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('delivery_detail', id=post.pk)

def delivery_add(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('delivery_detail', id=post.pk)
    else:
        form = DeliveryForm()
    context = {'form': form}
    return render(request, 'delivery_add.html', context)



##### FUNCTIONS
def today():
    return datetime.today().strftime('%Y-%m-%d')
