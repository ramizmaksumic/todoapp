from django.forms import ModelForm, fields, models
from .models import ToDoList

class ToDoForm(ModelForm):
    class Meta:
        model = ToDoList
        fields ="__all__"