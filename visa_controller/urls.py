from . import views
from django.urls import path

app_name = 'visa_controller'

urlpatterns = [
    path('', views.index, name='index'),
    path('action_index/', views.action_index, name='action_index'),
]