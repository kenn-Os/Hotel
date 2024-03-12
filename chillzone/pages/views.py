from django.shortcuts import render
from rooms.models import Rooms
# Create your views here.

def index(request):
    rooms = Rooms.objects.all()
    context = {
        'rooms': rooms
        
    } 
    
    return render(request, 'pages/index.html', context)
def about(request):
    return render(request, 'pages/about.html')
