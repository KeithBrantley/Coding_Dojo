from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime

# Create your views here.

# def index(request):
#     return HttpResponse("It's working")

def time(request):
    context = {
        'date': strftime("%b %d, %Y"),
        'time': strftime("%X %p"),
    }

    return render(request, "index.html", context)