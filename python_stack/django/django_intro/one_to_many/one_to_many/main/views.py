from django.shortcuts import render, redirect
from .models import Chef, Dish, Utensil

# Create your views here.

def index(request):
    context = {
        'all_chefs': Chef.objects.all(),
        'all_dishes': Dish.objects.all(),
        'all_utensils': Utensil.objects.all(),
    }
    return render(request, 'index.html', context)

def process_chef(request):
    Chef.objects.create(
        name=request.POST['name'],
        cuisine=request.POST['cuisine'],
        rank=request.POST['rank'],
    )
    return redirect('/')

def process_dish(request):
    this_chef = Chef.objects.get(id=request.POST["maker"])
    Dish.objects.create(
        name=request.POST["name"],
        tastiness_level=request.POST["tastiness_level"],
        spice=request.POST["spice"],
        maker=this_chef
    )
    return redirect('/')

def process_utensil(request):
    Utensil.objects.create(
        name=request.POST['name'],
        is_sharp=request.POST['is_sharp'],
    )
    return redirect('/')

def one_utensil(request, utensil_id):
    one_utensil = Utensil.objects.get(id=utensil_id)
    context={
        'one_utensil': one_utensil,
        'all_chefs': Chef.objects.all(),
    }
    return render(request, "one_utensil.html", context)

def add_user_utensil(request):
    one_utensil = Utensil.objects.get(id=request.POST['utensil_id'])
    one_chef = Chef.objects.get(id=request.POST['chef_id'])
    one_utensil.users.add(one_chef)
    return redirect(f'/utensil/{one_utensil.id}')