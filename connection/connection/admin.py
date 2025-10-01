from django.contrib import admin

from .models import product ,order
@admin.register(product,order)
class Admin(admin.ModelAdmin):
    list_display=['id']
