from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, QueryDict
from django.forms import formset_factory
from datetime import datetime, timedelta
from .models import *
from .forms import *
from django.forms import formset_factory

def index(request):
    next_week_forms = []
    #new orders to be creted.
    if (datetime.today().weekday() >0):
        days_to_monday = 7 - datetime.today().weekday()
        for i in range(5):
            date = (datetime.now() + timedelta(i+days_to_monday)).date()
            menus = Menu.objects.filter(Q(date__contains=date) | Q(is_forever=True)).all()
            next_week_forms.append({"date": date, "menus": menus})

    #actual orders.
    #get last monday. Get order one by one. If order == null, create blank order or form to be created.
    actual_week_orders = []
    context = {'actual_week_orders': actual_week_orders, 'next_week_forms': next_week_forms}
    return render(request, 'empresas/index.html', context)

def add_orders(request):
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

def get_next_day(weekday):
    return (datetime.today().weekday()+weekday+1)% 7

