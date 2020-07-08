from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.

def index(request):
    # context = {
    #     'all_users': User.object.all(),
    # }
    return render(request, 'index.html')


def new_user(request):
    return render(request, 'new_user.html')




