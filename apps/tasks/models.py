from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "task"
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.title