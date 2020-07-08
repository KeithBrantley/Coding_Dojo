from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def create(request):
    print("I'm going home")
    return redirect('/')

def show(request, num):
    return HttpResponse(f"Placeholder to edit blog {num}")

def edit(request, num):
    return HttpResponse(f"Placeholder edit blog number {num}")

def destroy(request, num):
    return redirect('/')
