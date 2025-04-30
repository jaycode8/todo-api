from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # owner = models.ForeignKey(User, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "todo"
        verbose_name = "todo"
        verbose_name_plural = "todos"

    def __str__(self):
        return self.title