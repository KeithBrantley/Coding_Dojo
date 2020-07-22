from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.

def add_a_show(request):
    return render(request, 'add_show.html')

def create_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect("/shows/new")

    created_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description']
    )
    return redirect(f'/shows/{created_show.id}')

def show_info(request, show_id):
    context ={
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'tv_show.html', context)

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')

def all_shows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "all_shows.html", context)

def edit(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)

def update(request, show_id):
    show = Show.objects.get(id=show_id)

    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect(f"/shows/{show_id}/edit")

    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()

    return redirect(f'/shows/{show_id}')