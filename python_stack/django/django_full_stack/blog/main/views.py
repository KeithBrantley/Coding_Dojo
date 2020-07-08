from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog

# Create your views here.

def index(request):
    context = {
        'bloggers': Blog.objects.all()
    }
    return render(request, 'index.html', context)

# def update(request, id):
#     # pass the post data to the method we wrote and save the response in a variable called errors
#     errors = Blog.objects.basic_validator(request.POST)
#         # check if the errors dictionary has anything in it
#     if len(errors) > 0:
#         # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
#         for key, value in errors.items():
#             messages.error(request, value)
#         # redirect the user back to the form to fix the errors
#         return redirect('/blog/edit/'+id)
#     else:
#         # if the errors object is empty, that means there were no errors!
#         # retrieve the blog to be updated, make the changes, and save
#         blog = Blog.objects.get(id = id)
#         blog.name = request.POST['name']
#         blog.desc = request.POST['desc']
#         blog.save()
#         messages.success(request, "Blog successfully updated")
#         # redirect to a success route
#         return redirect('/blogs')

def new_blogger(request):
    new_blogger = Blog.objects.create(
        name = request.POST['name'],
        desc = request.POST['desc']
    )

    return redirect('/')