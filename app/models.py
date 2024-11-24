from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        if self.completed:
            return f"{self.title} - {self.description} - Completed"
        else: 
            return f"{self.title} - {self.description} - Not Completed"
