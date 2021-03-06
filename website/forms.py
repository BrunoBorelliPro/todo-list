from django.forms import ModelForm
from website.models import ToDoItem
from django.db import models


class AddToDoItem(ModelForm):
    class Meta(models.Model):

        model = ToDoItem
        fields = ['name', 'description', 'status']
