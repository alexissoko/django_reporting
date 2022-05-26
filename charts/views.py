from django.shortcuts import render, redirect
from django.contrib.auth import logout as logouts
from .models import *
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView




def home(request):
    return render(request, 'welcome.html')


def reporting(request):

    mydict= {
        'sales':Sale.objects.values().order_by("-date"),
        'products':Product.objects.values().order_by("-date"),
        "df1" : sorted({x["date"].strftime('%Y-%m-%d'): x["quantity"] for x in Sale.objects.values().order_by("-date") if x["invoice_id"] == 1}.items()),
        "df2" : sorted({x["date"].strftime('%Y-%m-%d'): x["quantity"] for x in Sale.objects.values().order_by("-date") if x["invoice_id"] == 2}.items()),
        "df_labels" : list({x["date"].strftime('%Y-%m-%d') for x in Sale.objects.values().order_by("-date")}),
        }

    print("mydict")
    print(mydict["df1"])
    print(mydict["df2"])
    print(mydict["df_labels"])
    return render(request, 'index.html', context=mydict)

