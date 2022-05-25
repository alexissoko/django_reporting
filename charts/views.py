from django.shortcuts import render, redirect
from django.contrib.auth import logout as logouts
from .models import *
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView




def home(request):
    return render(request, 'welcome.html')


def reporting(request):
    # item = Sale.objects.order_by('date').values()
    item = Sale.objects.values()
    all_values = Sale.objects.all()
    all_items = set()
    for obj in all_values:
        if obj.invoice.name not in all_items:
            all_items.add(obj.invoice.name)

    df_params = {1: {}, 2: {}, 3: {}}
    for entry in item:
        if entry['date'].strftime('%Y-%m-%d') not in df_params[entry['invoice_id']]:
            df_params[entry['invoice_id']][entry['date'].strftime('%Y-%m-%d')] = entry['quantity']
        else:
            df_params[entry['invoice_id']][entry['date'].strftime('%Y-%m-%d')] += entry['quantity']
    df= pd.DataFrame(item)    
    df_labels= [str(x) for x in df.date.tolist()]
    df_labels= sorted(list(set(df_labels)))

    for year in df_labels:
        if year not in df_params[1]:
            df_params[1][year] = 0
        if year not in df_params[2]:
            df_params[2][year] = 0
        if year not in df_params[3]:
            df_params[3][year] = 0

    df1 = sorted(df_params[1].items())
    df2 = sorted(df_params[2].items())
    df3 = sorted(df_params[3].items())
    df1 = [x[1] for x in df1]
    df2 = [x[1] for x in df2]
    df3 = [x[1] for x in df3]
    
    mydict={
        'all_items':[str(x) for x in all_items],
        'df1':df1,
        'df2':df2,
        'df3':df3,
        'df_labels':df_labels
    }
    return render(request, 'index.html', context=mydict)

def logout(request):
    if request.method == "POST":
        logouts(request)
        return redirect('home')




"""
class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        # ""Return 7 labels for the x-axis.""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        # ""Return names of datasets.""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        # ""Return 3 datasets to plot.""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
# Create your views here.

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs=Sale.objects.all()
        
        labels = []
        default_items = []

        for item in qs:
            labels.append(item.date)
            default_items.append(item.quantity)

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
        
"""