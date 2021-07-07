from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import Vehicle_field , Engine_field

# Create your views here.

def home(request):
    if request.method=='GET':
        return render(request , 'tech_round_1/home.html',{'vehicle':Vehicle_field() , 'engine':Engine_field() })
    
    


