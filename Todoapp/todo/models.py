from django.db import models

class ToDoList(models.Model):
    task = models.CharField(max_length=256)
    is_completed = models.BooleanField(default=False)
    date_field = models.DateTimeField(auto_now_add=True)    

    def __str__(self) :
        return self.task