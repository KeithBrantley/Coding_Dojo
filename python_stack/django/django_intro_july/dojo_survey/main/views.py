from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create_result(request):
    your_name_from_form = request.POST['your_name']
    dojo_location_from_form = request.POST['dojo_location']
    favorite_language_from_form = request.POST['favorite_language']
    comment_from_form = request.POST['comment']
    context = {
        "your_name_on_template" : your_name_from_form,
        "dojo_location_on_template": dojo_location_from_form,
        "favorite_language_on_template": favorite_language_from_form,
        "comment_on_template": comment_from_form
    }
    return render(request, "result.html", context)

# def success(request):
#     return render(request, "result.html")
