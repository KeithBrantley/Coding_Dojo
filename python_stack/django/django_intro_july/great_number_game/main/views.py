from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def guess_num(request):
    number = request.POST['number']
    rand_num = random.randint(1, 100)
    if number < rand_num:
        
    print(rand_num)