from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


from home.models import Tasks


# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['desc']
        ins = Tasks(taskName=name, taskDesc=desc)
        ins.save()
        request.user.Tasks.add(ins)
        messages.success(request, "Success Task Added")

    return render(request, 'index.html')


def tasks(request):
    allTasks = Tasks.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)


def delete(request, pk):
    task = Tasks.objects.filter(pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse('tasks'))
