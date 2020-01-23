from . import views
from django.urls import path

app_name = 'visa_controller'

urlpatterns = [
    path('', views.index, name='index'),
    path('connect/', views.connect, name='connect'),
    path('measure/', views.measure, name='measure'),
]