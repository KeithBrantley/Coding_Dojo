from django.shortcuts import render, HttpResponse, redirect, render

# Create your views here.

def index(request):
    return render(request, "index.html")
    # return HttpResponse('This is actually fun!')

def checkout_page(request):
    return render(request, "checkout.html")

def checkout(request):
    print(request.POST)
    return HttpResponse('This is the checkout page')

def check_total(request, check_out_total):
    return HttpResponse(f'I purchaseed {check_out_total} this session.')

def direct_to_index(request):
    print('I am going to the home page!')
    return redirect('/')


