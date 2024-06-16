from django.shortcuts import render
from datetime import datetime

# Create your views here.
def filter(request):
    message="Hii hello Good Morning"
    animal="pig"
    p=10
    dt=datetime.now
    d={'msg':message,'animal':animal,'p':p,'dt':dt}
    return render(request,'filter.html',d)

