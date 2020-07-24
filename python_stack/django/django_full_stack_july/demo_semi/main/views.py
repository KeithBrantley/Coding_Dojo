from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Show, Network
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')
    hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        f_name=request.POST['first_name'],
        l_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hash
    )
    request.session['user_id'] = new_user.id
    return redirect('/shows')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')
    user = User.objects.filter(email=request.POST['login_email'])
    if user:
        user = user[0]
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/shows')
        messages.error(request, "passwords do not match!")
    return redirect('/')

def all_shows(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'shows.html', context)

def add_show(request):
    return render(request, 'new_show.html')

def process_show(request):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.errors(request, msg)
        return redirect('/add_show')
    if len(request.POST['network1']) != 0:
        network = Network.objects.create(name=request.POST['network1'])
    else:
        network = Network.objects.get(name=request.POST['network2'])
    user = User.objects.get(id=request.session['user_id'])
    new_show = Show.objects.create(
        title=request.POST['title'],
        network=network,
        release_date=release_date,
        submitted_by=user,
        description=request.POST['description']
    )
    return redirect(f'/shows/{new_show.id}')

def logout(request):
    request.session.flush()
    return redirect('/')
