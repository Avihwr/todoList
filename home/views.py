from django.shortcuts import render
from home.models import Tasks


# Create your views here.

def home(request):
    context = {'success': False}
    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['desc']
        ins = Tasks(taskName=name, taskDesc=desc)
        ins.save()
        request.user.Tasks.add(ins)
        context = {'success': True}

    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Tasks.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)
