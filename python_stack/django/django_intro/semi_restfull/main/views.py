from django.shortcuts import render, redirect
from . models import Show
from django.contrib import messages

# Create your views here.

def add_new_show(request):
    return render(request, 'add_show.html')

# Creates a Show
def create_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/shows/new')

    created_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect(f'/shows/{created_show.id}')

# Show's detail page
def show_details(request, show_id):
    context={
        'this_show': Show.objects.get(id=show_id)
    }
    return render(request, 'show_details.html', context)

# Deletes a show
def delete_show(request, show_id):
    deleted_show = Show.objects.get(id=show_id)
    deleted_show.delete()

    return redirect('/shows')

# all shows page
def all_shows(request):
    context={
        'shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

# edits a show
def edit(request, show_id):
    show_date = Show.objects.get(id=show_id)
    show_date.release_date = show_date.release_date.strftime('%Y-%m-%d')
    context={
        'show': show_date
    }
    return render(request, 'edit.html', context)

# updates a show
def update(request, show_id):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect(f'/shows/{show_id}/edit')

    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f'/shows/{show_id}')

