from django.db import models


class ToDoItem(models.Model):
    STATUS_OPTIONS = (
        ('TD', 'TO DO'),
        ('DO', 'DOING'),
        ('CM', 'COMPLETED')
    )
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    status = models.CharField(max_length=2, choices=STATUS_OPTIONS, default='TD')
