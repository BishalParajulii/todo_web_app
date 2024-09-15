from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.



def index(request):
    task = Task.objects.all()

    form  = TaskForm()

    context = {'tasks' : task , 'form' : form}

    if request.method  == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    return render(request , 'task/list.html' , context)



def updateTask(request ,pk):


    task = Task.objects.get(id = pk)

    form = TaskForm(instance = task)

    context = {'form' : form }


    if request.method == "POST":
        form = TaskForm(request.POST  , instance = task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request , 'task/update_task.html' , context)
