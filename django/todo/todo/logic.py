from . import models

def create_and_save_new_task(task_name):
    new_task = models.Task(task_name=task_name)
    new_task.save()

def create_and_save_new_item(item_name, task):
    new_ie = models.Item(
        item_name = item_name,
        task = task,
        )
    new_ie.save()


def get_all_tasks():
    return models.Task.objects.all()


def get_all_items():
    return models.Item.objects.all()

def get_all_items_for_task(task):
    return models.Item.obects.filter(task=task)

def get_task_to_items_dict():
    task_to_items = {}
    items = []
    tasks = models.Task.objects.all()

    for task in tasks:
        for item in models.Item.objects.filter(task=task):
            items.append(item.item_name)
        task_to_items[task.task_name] = items
        items = []

    return task_to_items


def get_task_by_name(task_name):
    task_object_list = models.Task.objects.filter(task_name=task_name)
    task_object = task_object_list[0]
    return task_object

def save_text_as_item(new_item_text, task_object):
    new_item = models.Item(
        item_name=new_item_text,
        task=task_object,
    )
    new_item.save()

def delete_item_by_name(item_name):
    item = models.Item.objects.filter(item_name=item_name)
    item.delete()

def save_task(new_task):
    new_task = models.Task(
        task_name=new_task,
    )
    print(new_task)
    new_task.save()



# def create_task_to_items():
#     task_to_items = {}
#     items = models.Item.objects.all()
#     for item in items:
#         if task_to_items[item.task.task_name]:
#             task_to_items[item.task.task_name].append(item.item_name)
#         else:
#             task_to_items[item.task.task_name] = [item.item_name]
#
#     print(task_to_items)
#     return task_to_items
