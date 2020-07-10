from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_user(request):
    print("Got Post Info....................")
    first_name_from_form = request.POST['first_name']
    last_name_from_form = request.POST['last_name']
    email_from_form = request.POST['email']
    context = {
        "first_name_on_template" : first_name_from_form,
        "last_name_on_template" : last_name_from_form,
        "email_on_template" : email_from_form
    }
    return redirect('/success')

def success(request):
    return render(request, "success.html")
