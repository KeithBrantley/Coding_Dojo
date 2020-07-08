from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("Testy Test")

def bananas(request):
    return HttpResponse("This is bananas! B A N A N A S!")

def nanners_in_bunch(request, num_of_nanners):
    return HttpResponse(f"I have {num_of_nanners} in my bunch")

def direct_to_index(request):
    print("I am going home!!")
    return redirect('/bananas')

def simple_page(request):
    return render(request, "simple.html")
