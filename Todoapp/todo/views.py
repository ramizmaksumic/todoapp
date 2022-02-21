from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import ToDoList
from . import forms
from .forms import ToDoForm

def home(request):
    todos = ToDoList.objects.all()

    form = ToDoForm()

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {'todos':todos,'form':form}
    return render(request, 'todo/home.html',context)

def update(request,pk):
    todo = ToDoList.objects.get(id=pk)

    form = ToDoForm(instance=todo) 
    if request.method == 'POST':
        form = ToDoForm(request.POST,instance=todo) 
        if form.is_valid():
            form.save()
        return redirect('/')

    context ={'form':form}
    return render(request, 'todo/update.html',context)

def delete(request,pk):
    todo = ToDoList.objects.get(id=pk)

    form = ToDoForm(instance=todo)

    if request.method == 'POST':
        todo = ToDoList.objects.get(id=pk).delete()
        return redirect('/')

        

    context ={'form':form,'todo':todo}
    return render(request, 'todo/delete.html',context)