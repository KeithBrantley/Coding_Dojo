from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        'all_dojos': Dojo.objects.all(),
        'all_ninjas': Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def process_dojo(request):
    Dojo.objects.create(
        name=request.POST["name"],
        city=request.POST["city"],
        state=request.POST["state"] 
    )
    return redirect('/')

def process_ninja(request):
    this_dojo = Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        dojo=this_dojo
    )
    return redirect('/')

def delete_dojo(request, dojo_id):
    Dojo.objects.get(id = dojo_id).delete()
    return redirect('/')