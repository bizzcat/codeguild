from django.db import models


class Task(models.Model):
    task_name = models.TextField()
    


    def __str__(self):
        return self.task_name


    def __repr__(self):
        return 'List(action={!r})'.format(self.task_name)


class Item(models.Model):
    item_name = models.TextField()
    task = models.ForeignKey(Task)


    def __str__(self):
        return self.item_name

    def __repr__(self):
        return 'Task Item(item={!r})'.format(self.item_name)
