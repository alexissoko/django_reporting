from django.shortcuts import render, redirect
from django.contrib.auth import logout as logouts
from .models import *
from .forms import *
# import pandas as pd
# from rest_framework.views import APIView
# from rest_framework.response import Response
import json

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# from chartjs.views.lines import BaseLineChartView



def home(request):
    return render(request, 'welcome.html')

@login_required
def reporting(request):
    if request.GET.get("begin"):
        mesh_from = request.GET.get("begin")
    else:
        mesh_from = "2000-01-01"
    if request.GET.get("until"):
        mesh_to = request.GET.get("until")
    else:
        mesh_to = timezone.now().strftime('%Y-%m-%d')
    sales = Sale.objects.filter(date__range=[mesh_from, mesh_to]).order_by("-date")

    all_data = {prod.invoice.name: {} for prod in sales}
    df_labels = sorted([x[0].strftime('%Y-%m-%d') for x in sales.values_list("date").distinct()])

    for sale in sales:
        all_data[sale.invoice.name][sale.date.strftime('%Y-%m-%d')] = sale.quantity
    
    for label in df_labels:
        for k, v in all_data.items():
            if label not in v:
                all_data[k][label] = 0
    
    for k,v in all_data.items():
        all_data[k] = [all_data[k][x] for x in sorted(all_data[k])]

    print("df_labels")
    print(df_labels)
    print("all_data")
    print(all_data)
    labels = list(all_data.keys())
    values = list(all_data.values())
    


    mydict= {
        'sales':sales,
        'products':Product.objects.values().order_by("-date"),
        "all_data" : sorted(all_data),
        "df1" : sorted({x["date"].strftime('%Y-%m-%d'): x["quantity"] for x in sales.values().order_by("-date") if x["invoice_id"] == 1}.items()),
        "df_labels" : df_labels,
        "labels" : labels,
        "values" : values,
    
    }
    return render(request, 'index.html', context=mydict)

