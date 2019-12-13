from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, QueryDict
from django.forms import formset_factory
from datetime import datetime, timedelta
from .models import *
from .forms import *
from django.forms import formset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import empresas.constants as C

def login_user(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(C.INDEX_URL)
        else:
            messages.error(request, C.LOGIN_MESSAGE_ERROR)
            return redirect(C.LOGIN_URL)
    return render(request, C.LOGIN_TEMPLATE, {"title": C.LOGIN_TITLE})

@login_required(login_url=C.LOGIN_URL)
def index(request):
    next_week_forms = []
    #new orders to be creted.
    if (datetime.today().weekday() > 0):
        days_to_monday = 7 - datetime.today().weekday()
        for i in range(5):
            date = (datetime.now() + timedelta(i+days_to_monday)).date()
            menus = Menu.objects.filter(Q(date__contains=date) | Q(is_forever=True)).all()
            try:
                order = Order.objects.get(id_empleado=request.user, date__contains=date)
                id_menu = order.id_menu.id
            except Order.DoesNotExist:
                id_menu = -1
            next_week_forms.append({"date": date, "menus": menus, "id_menu": id_menu})
    #actual orders.
    #get last monday. Get order one by one. If order == null, create blank order or form to be created.
    
    last_monday = (datetime.now() - timedelta(datetime.today().weekday()))
    actual_week_orders = []
    for i in range(5):
        date = (last_monday + timedelta(i)).date()
        try:
            order = Order.objects.get(id_empleado=request.user, date__contains=date)
        except Order.DoesNotExist:
            order = Order(id_empresa=request.user.empresa, id_empleado=request.user, id_menu=None, date=date)
        actual_week_orders.append(order)
    #ACTUAL ORDERS NO MOSTRAR MENUES QUIZA, SOLO EL ELEGIDO
    context = {'title': C.INDEX_TITLE, 'actual_week_orders': actual_week_orders, 'next_week_forms': next_week_forms}
    return render(request, C.INDEX_TEMPLATE, context)

def order_add(request):
    if request.method == "POST":
        for key in filter(lambda x: x != "csrfmiddlewaretoken", request.POST):
            try:
                menu = Menu.objects.get(pk=request.POST[key])
                order = Order.objects.get(id_empleado=request.user, date__contains=datetime.strptime(key, '%d-%m-%y').date())
                order.id_menu = menu
                order.save()
            except Order.DoesNotExist:
                order = Order(id_empresa=request.user.empresa, id_empleado=request.user, id_menu=menu, date=datetime.strptime(key, '%d-%m-%y'))
                order.save()
            except Exception as e:
                print(e)
            
        return redirect(C.APP_ROOT_PATH)

def get_next_day(weekday):
    return (datetime.today().weekday()+weekday+1)% 7

