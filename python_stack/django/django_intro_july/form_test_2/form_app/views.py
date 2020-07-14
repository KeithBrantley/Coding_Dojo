from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_user(request):
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email'] = request.POST['email']
    request.session['comment'] = request.POST['comment']
    context = {
        "first_name" : request.session['first_name'],
        "last_name": request.session['last_name'],
        "email": request.session['email'],
        "comment": request.session['comment'],
    }
    return redirect('/success')

def success(request):
    print(request.session)
    return render(request, 'success.html')