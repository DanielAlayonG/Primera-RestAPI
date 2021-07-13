from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    #Se define que campos se mostraran en el menu todo
    list_display = ("title", "description", "completed")
    #Se crea la opcion de filtrar entre tareas completadas, no completadas, o ambas
    list_filter = ("completed",)

admin.site.register(Todo, TodoAdmin)