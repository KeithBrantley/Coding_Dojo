# from django.shortcuts import render, HttpResponse, redirect
# import random randrange
# from datetime import datetime

# # Create your views here.
# def index(request):
#     request.POST["name"]
    
#     return render(request, "index.html")

# def success(request):
#     print(request.session.keys())
#     context = {
#         'location': request.session['location_of_work']
#         'amount': request.session['amount_of_gold']
#         ''
#     }
#     return render(request, 'index.html', context)

# def reset(reset, sum):
#     sum = 0
#     request.session.clear()
#     return redirect(render('/'))


# def process_money(request, sum):
#     if (x == 'farm'):
#         gold = randrange(10,20)
#         sum += gold
#         print(f"You earned {gold} from the farm! {time}")
#     elif (x == 'cave'):
#         gold = randrange(5,10)
#         sum += gold
#         print(f"You earned {gold} from the cave! {time}")
#     elif (x == 'house'):
#         gold = randrange(2,5)
#         sum += gold
#         print(f"You earned {gold} from the house! {time}")
#     elif (x == 'casino'):
#         gold = randrange(-50,50)
#         sum += gold
#         if (randint() > 0):
#             print(f"Entered a casino and gained {gold} gold....Wewt! {time}")
#         elif (randint() < 0):
#             print(f"Entered a casino and lost {gold} gold...Ouch... {time}")
#     return sum    
#     return redirect(request, '/')


# Code from Video (all of it)
# def index(request):
#   print(request.session.keys())
#   context={'key:42}
#   return render(request, index.html, context)

# def process(request)
#   print(request.session)
#   print(request.session.keys())
#   print("earned gold, sending back to home page")
#   if 'location_from_game' not in request.session:
#       request.session('location_from_game)
#       print('I has a location yey', request.session[location_from_game])
#       request.session['gold_total'] = request.POST['gold_total']
#       request.session['time_gold_earned']
#       return redirect('/process_money')

# def success(request):
#   

# input: X amount of locations that user earned gold from (or clicked the button)
# output: session history with the 2 names submitted from the form


from django.shortcuts import render, HttpResponse, redirect
from time import strftime
import random

def index(request):
    return render(request, 'index.html')

def process_money(request):
    if 'count' in request.session:
        if request.POST['building'] == 'farm':
            score = random.randint(10,20)
        elif request.POST['building'] == 'cave':
            score = random.randint(5,10)
        elif request.POST['building'] == 'house':
            score = random.randint(2,5)
        elif request.POST['building'] == 'casino':
            score = random.randint(-50,50)
        request.session['count'] += score
        if score > 0:
            request.session['box'].insert(0,{'class': 'green', 'log': f"You earned {score} golds from the {request.POST['building']}! {strftime('%Y/%m/%d %I:%M:%S %p')}"})
        else:
            request.session['box'].insert(0,{'class': 'red', 'log': f"You lost {-1*score} golds at the {request.POST['building']}... Ouch!!! {strftime('%Y/%m/%d %I:%M:%S %p')}"})
    else:
        request.session['count'] = 0
        request.session['box'] = []
    return redirect('/')

def reset(request):
    request.session['count'] = 0
    request.session['box'] = []
    return redirect('/')
