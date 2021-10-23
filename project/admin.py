import form as form
from django.contrib import admin

from .models import Profile
from . import models

# Register your models here.

# admin.site.register(models.Medicine)


admin.site.register(models.Profile)


@admin.register(models.Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('title', 'SUPPLIED_TYPE', 'updated',)
    list_filter = ('SUPPLIED_TYPE', 'updated')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('SUPPLIED_TYPE', 'title')
    date_hierarchy = 'updated'
