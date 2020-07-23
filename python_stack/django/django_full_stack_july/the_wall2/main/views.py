from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
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
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hash
    )
    request.session['user_id'] = new_user.id
    return redirect('/wall')

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
            return redirect('/wall')
        messages.error(request, "passwords do not match!")
    return redirect('/')

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    elif 'user_id' in request.session:
        context = {
            'username': User.objects.get(id = request.session['user_id']),
            'all_messages':reversed(Message.objects.all()),
            'user_id': request.session['user_id'],
        }
        return render(request, 'comments.html',context)

    # return render(request, 'comments.html')

def logoff(request):
    request.session.flush()
    return redirect('/')
