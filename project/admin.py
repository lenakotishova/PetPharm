from django.contrib import admin
from . import models


# Register your models here.

# admin.site.register(models.Medicine)
admin.site.register(models.Profile)


@admin.register(models.Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'SUPPLIED_TYPE', 'updated',)
    list_filter = ('SUPPLIED_TYPE', 'created')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('SUPPLIED_TYPE', 'title')
    radio_fields = {"PHARMACY": admin.VERTICAL}

