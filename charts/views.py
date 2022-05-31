from django.shortcuts import render, redirect
from django.contrib.auth import logout as logouts
from .models import *
from .forms import *
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView




def home(request):
    return render(request, 'welcome.html')

@login_required
def reporting(request):
    if request.GET.get("begin"):
        print("begin")
        print(request.GET.get("begin"))
        mesh = request.GET.get("begin")

        sales = Sale.objects.filter(date__range=[mesh, timezone.now().strftime('%Y-%m-%d')]).order_by("-date")
    else:
        print("Ouch")
        print(request)
        sales = Sale.objects.all().order_by("-date")

    data = {prod.invoice.name: {} for prod in sales}
    labels = sorted([x[0].strftime('%Y-%m-%d') for x in sales.values_list("date")])
    print("labels")
    print(labels)
    for sale in sales:
        data[sale.invoice.name][sale.date.strftime('%Y-%m-%d')] = sale.quantity
    
    print("data")
    print(data)
    mydict= {
        'sales':sales,
        'products':Product.objects.values().order_by("-date"),
        "data" : sorted(data),
        "df1" : sorted({x["date"].strftime('%Y-%m-%d'): x["quantity"] for x in sales.values().order_by("-date") if x["invoice_id"] == 1}.items()),
        "df2" : sorted({x["date"].strftime('%Y-%m-%d'): x["quantity"] for x in sales.values().order_by("-date") if x["invoice_id"] == 2}.items()),
        "df_labels" : labels
    }
    return render(request, 'index.html', context=mydict)

