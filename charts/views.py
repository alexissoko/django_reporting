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

    all_data = {prod.invoice.name: {} for prod in sales}

    df_labels = sorted([x[0].strftime('%Y-%m-%d') for x in sales.values_list("date").distinct()])

    sales.values().order_by("-date")
    for sale in sales:
        all_data[sale.invoice.name][sale.date.strftime('%Y-%m-%d')] = sale.quantity
    
    for label in df_labels:
        for k, v in all_data.items():
            if label not in v:
                all_data[k][label] = 0
    
    for k,v in all_data.items():
        all_data[k] = [all_data[k][x] for x in sorted(all_data[k])]
    print("all_data")
    labels = list(all_data.keys())

    mydict= {
        'sales':sales,
        'products':Product.objects.values().order_by("-date"),
        "all_data" : sorted(all_data),
        "df1" : sorted({x["date"].strftime('%Y-%m-%d'): x["quantity"] for x in sales.values().order_by("-date") if x["invoice_id"] == 1}.items()),
        "df_labels" : df_labels,
        "labels" : labels,
        # "df1" : sorted({x["date"].strftime('%Y-%m-%d'): x["quantity"] for x in sales.values().order_by("-date") if x["invoice_id"] == 1}.items()),
        # "df2" : sorted({x["date"].strftime('%Y-%m-%d'): x["quantity"] for x in sales.values().order_by("-date") if x["invoice_id"] == 2}.items()),
        "df1" : all_data["Mil hojas"],
        "df2" : all_data["Flan casero"]
    
    }
    return render(request, 'index.html', context=mydict)

