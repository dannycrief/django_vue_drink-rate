from django.contrib import admin
from .models import Drink


@admin.register(Drink)
class DinkAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'rating']
