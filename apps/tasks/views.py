from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')

        # Удаление задачи
        if task_id and 'delete' in request.POST:
            get_object_or_404(Task, id=task_id).delete()

        # Редактирование задачи
        elif task_id and len(request.POST) > 3:
            task = get_object_or_404(Task, id=task_id)
            task.title = request.POST.get('title', task.title)
            task.description = request.POST.get('description', task.description)
            task.status = request.POST.get('status') == 'True'
            task.save()

        # Создание задачи
        else:
            title = request.POST.get('title')
            description = request.POST.get('description')

            if title and description:
                Task.objects.create(title=title, description=description)

    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'main.html', context)
