from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    print("index")
    return render(request, 'visa_controller/index.html')

def action_index(request):
    redirect_url = reverse('visa_controller:index')
    print(redirect_url)
    if request.method == 'GET':
        if 'VPP' in request.GET:
            print("cout: VPP")
        if 'VMAX' in request.GET:
            print("cout: VMAX")
    return redirect('visa_controller:index')