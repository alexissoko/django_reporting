from django.shortcuts import render
from .models import *
import pandas as pd

# Create your views here.
def home(request):
    item = Sale.objects.all().values()
    df= pd.DataFrame(item)
    df1= [str(x) for x in df.date.tolist()]
    df= df['quantity'].tolist()
    mydict={
        'df':df,
        'df1':df1
    }
    return render(request, 'index.html', context=mydict)