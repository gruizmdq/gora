from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, QueryDict
from django.forms import formset_factory
from datetime import datetime
from .models import *
from .forms import *
import gestor.constants as C

def index(request):
    today_orders = Order.objects.filter(date__contains = today()).order_by('-date') 
    context = {'orders': today_orders}
    print(len(today_orders))
    return render(request, 'index.html', context)



#### ORDERS #############

def orders(request):
    today_orders = Order.objects.order_by('-date')[:10]
    context = {'orders': today_orders}
    print(len(today_orders))
    return render(request, C.ORDER_INDEX, context)


def order_detail(request, id):
    if request.method == "POST":
        try:
            instance = Order.objects.get(pk=id)
        except Order.DoesNotExist:
            raise Http404("Order does not exist")
        form = OrderForm(request.POST or None, instance=instance)
        if form.is_valid():
            post = form.save(commit=False)
            post.qty = sum(int(x) for x in request.POST.getlist("qty[]"))
            post.save()
            if post:
                index = 0
                #delete previous order_items
                Order_Item.objects.filter(id_order = id).all().delete()
                for i in request.POST.getlist("qty[]"):
                    index += 1
                    key_type = "order-type-" + str(index)
                    item_form = TypeOrderForm({"id_order": post.pk, "qty": i, "order_type": request.POST.get(key_type)})
                    if item_form.is_valid():
                            item_form.save()
                    else:
                        print("Tirar Excepcionnnnn")

            return redirect(C.ORDER_DETAIL, id=post.pk)
    else:
        try:
            order = Order.objects.get(pk=id)
            items = Order_Item.objects.filter(id_order = id).values()
        except Order.DoesNotExist:
            raise Http404("Order does not exist")
        form = OrderForm(instance=order)
    return render(request, C.ORDER_DETAIL, {'form': form, 'items': items})

def order_add(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.qty = sum(int(x) for x in request.POST.getlist("qty[]"))
            post.save()
            if post:
                index = 0
                for i in request.POST.getlist("qty[]"):
                    index += 1
                    key_type = "order-type-" + str(index)
                    item_form = TypeOrderForm({"id_order": post.pk, "qty": i, "order_type": request.POST.get(key_type)})
                    if item_form.is_valid():
                            item_form.save()
                    else:
                        print("Tirar Excepcionnnnn")

            return redirect(C.ORDER_DETAIL, id=post.pk)
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, C.ORDER_ADD, context)


##### DELIVERY ##########
def delivery(request):
    deliverys = Delivery.objects.all()
    for d in deliverys:
        d.orders_pending = Order.objects.filter(delivery_assigned_id = d.id).exclude(state = C.ORDER_STATE_SUCCESS).count()  
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
