from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, QueryDict
from django.forms import formset_factory
from datetime import datetime, timedelta
from .models import *
from .forms import *
from django.forms import formset_factory

def index(request):
    if (datetime.today().weekday() >3):
        days_to_monday = 7 - datetime.today().weekday()
        next_week_forms = []
        for i in range(5):
            date = (datetime.now() + timedelta(i+days_to_monday)).date()
            #menus = Menu.objects.filter(Q(date__contains=date) | Q(is_forever=True)).all()
            next_week_forms.append(OrderForm(initial={'date': date}, date=date))
            print(next_week_forms)

    form = OrderForm(initial={'date': django.utils.timezone.now})
    context = {'form': form, 'next_week_forms': next_week_forms}
    return render(request, 'empresas/index.html', context)

def get_next_day(weekday):
    return (datetime.today().weekday()+weekday+1)% 7

