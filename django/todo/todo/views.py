from django.shortcuts import render

from . import logic


def render_index(request):
    task_to_items = logic.get_task_to_items_dict()

    template_args = {
        'task_to_items': task_to_items,
    }
    return render(request, 'todo/index.html', template_args)


def add_item_and_refresh(request, task_name):
    task_object = logic.get_task_by_name(task_name)
    new_item_text = request.POST['name']
    logic.save_text_as_item(new_item_text, task_object)
    return render_index(request)

def delete_item_and_refresh(request, item_name):
    logic.delete_item_by_name(item_name)
    return render_index(request)


def add_task_and_refresh(request):
    new_task = request.POST['name']
    logic.save_task(new_task)
    return render_index(request)
