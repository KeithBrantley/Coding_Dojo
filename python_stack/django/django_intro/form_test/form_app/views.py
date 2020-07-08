from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def create_user(request):
    print('Got post Info..............')
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form 
    }
    # print(name_from_form)
    # print(email_from_form)
    # print(request.POST)
    return render(request,"show.html",context)

def success(request):
    return render(request, "success.html")

def some_function(request):
    request.session['namne'] = request.POST['name']
    request.session['counter'] = 100