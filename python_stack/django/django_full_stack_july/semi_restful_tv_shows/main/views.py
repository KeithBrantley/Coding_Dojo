from django.shortcuts import render
from .models import Show

# Create your views here.


def index(request):
    return render(request, 'add_show.html')


def add_a_show(request):
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description']
    )
    return render(request, 'tv_show.html')

def view_show()
