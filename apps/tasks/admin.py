from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','status','updated_at')
    search_fields = ('title',)
    list_filter = ('title','status','created_at','updated_at')
