from django.contrib import admin

# Importing new Model
from .models import TodoItem

# Register your models here.

admin.site.register(TodoItem)  # registering new Model
