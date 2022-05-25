from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reporting/', views.reporting, name='reporting'),
]  # end urlpatterns