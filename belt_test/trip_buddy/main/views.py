from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import User, Trip
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'login.html')


def register(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')
    hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hash
    )
    request.session['user_id'] = new_user.id
    return redirect('/dashboard')

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
            return redirect('/dashboard')
        messages.error(request, "passwords do not match!")
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'trips': Trip.objects.all(),
    }
    return render(request, 'dashboard.html', context)

def create_new_trip_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'new_trip.html')

def create_trip(request):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors):
        for error in errors.values():
            messages.error(request, error)
        return redirect('/create_new_trip_page')
    else:
        Trip.objects.create(
            destination = request.POST['destination'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            plan = request.POST['plan'],
            user = User.objects.get(id = request.session['user_id'])
        )
        print(request.POST)
        return redirect('/dashboard')

def edit_trip(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'trip': Trip.objects.get(id=trip_id),
        'user': User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'edit.html', context)

def update(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Trip.objects.edit_validator(request.POST)
    if len(errors):
        for error in errors.values():
            messages.error(request, error)
        return redirect(f'/dashboard/update/{trip_id}')
    else:
        update = Trip.objects.get(id=trip_id)
        update.destination = request.POST['destination']
        update.start_date = request.POST['start_date']
        update.end_date = request.POST['end_date']
        update.plan = request.POST['plan']
        update.save()
        return redirect('/dashboard')

def view_trip(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context={
        'trip': Trip.objects.get(id=trip_id),
        'user': User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'view.html', context)

def delete(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')
    Trip.objects.get(id=trip_id).delete()
    return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')
