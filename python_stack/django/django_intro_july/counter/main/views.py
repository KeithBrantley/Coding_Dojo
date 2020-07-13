from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return render(request, 'index.html')

def delete_session(request):
    del request.session['counter']
    return redirect('/')
