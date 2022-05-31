from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reporting/<begin>', views.reporting, name='reporting-param'),
    path('reporting/', views.reporting, name='reporting'),
]  # end urlpatterns