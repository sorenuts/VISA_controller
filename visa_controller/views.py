from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from . import visafunc

# Create your views here.
def index(request):
    print("index")
    return render(request, 'visa_controller/index.html')

def connect(request):
    redirect_url = reverse('visa_controller:index')
    if visafunc.connect_VISA() != 0:
        print("connection failed.")
    query_out = visafunc.measure_IDN()
    return render(request, 'visa_controller/index.html',  {'query_out' : query_out})

def measure(request):
    redirect_url = reverse('visa_controller:index')
    print(redirect_url)
    if request.method == 'GET':
        if 'VPP' in request.GET:
            print("cout: VPP")
            query_out = visafunc.measure_VPP()
        if 'VMAX' in request.GET:
            print("cout: VMAX")
    return render(request, 'visa_controller/index.html',  {'query_out' : query_out})