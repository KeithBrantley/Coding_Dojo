from django.shortcuts import render
from .models import User

# Create your views here.

def index(request):
    print(User.objects.all())
    context ={
        "all_users": User.objects.all()
    }
    return render(request, 'index.html', context)