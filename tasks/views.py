from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Task


# Create your views here.
def addTask(request):
    if request.method=='POST':
        task = request.POST['task']
        instance = Task(task = task)
        instance.save()
        
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    
    return redirect('home')

def undone(request, pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
        
    else:
        context ={
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)