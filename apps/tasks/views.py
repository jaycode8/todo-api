from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer