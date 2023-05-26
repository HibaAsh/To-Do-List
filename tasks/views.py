from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def homePage(request):
    tasks = Task.objects.all().order_by('title')
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")

    context = {'tasks':tasks, 'form':form}
    return render(request, "tasks/homePage.html", context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

        return redirect("tasks:homePage")

    context = {'form':form}

    return render(request, "tasks/update_task.html", context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    form = deleteForm()

    if request.method == "POST":
        form = deleteForm(request.POST)
        if form.is_valid():
            yes = form.cleaned_data.get("yes")
            no = form.cleaned_data.get("no")
            if yes:
                item.delete()
            return redirect("tasks:homePage")

    context = {'item':item, 'form':form}
    return render(request, "tasks/delete_task.html", context)