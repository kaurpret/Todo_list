from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.models import User, auth

def todo(request):
    return render(request,'todos.html')

    
#  To Create data
def submit(request):
    if request.method=="POST":
        title = request.POST["title"]
        description = request.POST["description"]
        priority = request.POST["priority"]
        obj = data(title=title,description=description,priority=priority)
        obj.save()
        c= data.objects.all()
        return render(request, 'todo1.html',{'result':c} )


# to delete a record  
def delete(request, id):
    obj = data.objects.get(id = id)
    obj.delete()
    c = data.objects.all()
    return render(request, 'todo1.html' , {'result':c})
    
#  used list added data

def list_item(request):
    c = data.objects.all()
    return render(request, 'todo1.html' , {'result':c})

# used to sort data

def sort(request):
    c = data.objects.order_by('priority')
    return render(request, 'todo1.html' , {'result':c})

#  For searching

def search(request):
    if request.method == "POST":
        s= request.POST['search']
        c = data.objects.filter(title__contains=s)
        return render(request, 'todo1.html' ,{'result':c})


#  To edit in data

def edit(request,id):
    obj = data.objects.get(id = id)
    c = {
        "title" : obj.title,
        "description" : obj.description,
        "priority" : obj.priority,
        "id": obj.id,
    }

    return render(request, 'todo2.html' , context = c)

# To update data

def update(request,id):
    obj = data.objects.get(id = id)
    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.priority = request.POST['priority']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at= updated_at
    obj.save()
    c = data.objects.all()
    return render(request, 'todo1.html',{'result':c} )







