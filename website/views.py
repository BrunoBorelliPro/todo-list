from django.http import HttpResponse
from django.shortcuts import render
from website.models import ToDoItem
from website.forms import AddToDoItem


def list_todo_items(request):

    if request.method == 'POST':
        if request.POST.get('deletar'):
            delete_item = ToDoItem.objects.get(id=request.POST['itemId'])
            delete_item.delete()
        elif request.POST.get('do'):
            altera_item = ToDoItem.objects.get(id=request.POST['itemId'])
            altera_item.status = 'DO'
            altera_item.save()
            pass
        elif request.POST.get('to_do'):
            altera_item = ToDoItem.objects.get(id=request.POST['itemId'])
            altera_item.status = 'TD'
            altera_item.save()
        elif request.POST.get('complete'):
            altera_item = ToDoItem.objects.get(id=request.POST['itemId'])
            altera_item.status = 'CM'
            altera_item.save()
        else:
            name = request.POST['name']
            description = request.POST['description']
            status = request.POST['status']
            to_do_item = ToDoItem()
            to_do_item.name = name
            to_do_item.description = description
            to_do_item.status = status
            to_do_item.save()
            pass

    context = {
        'items_todo': ToDoItem.objects.all().filter(status='TD'),
        'items_doing': ToDoItem.objects.all().filter(status='DO'),
        'items_complete': ToDoItem.objects.all().filter(status='CM'),
        'options': ToDoItem.STATUS_OPTIONS,
        'form': AddToDoItem()
    }
    return render(request, 'ToDoList.html', context)
