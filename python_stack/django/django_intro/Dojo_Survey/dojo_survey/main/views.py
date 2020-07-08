from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def results(request):
    name = request.POST["name"]
    dojo_location = request.POST["dojo_location"]
    # fav_language = request.POST["fav_language"]
   
    return redirect(f'/success/{name}/{dojo_location}')

def success(request, name, dojo_location):
    context = {
        "name_from_form": name,
        "dojo_location_from_form": dojo_location,
        # "favorite_language_from_form": fav_language,
}
    return render(request, 'results.html', context)


def direct_to_index(request):
    return redirect('/')
