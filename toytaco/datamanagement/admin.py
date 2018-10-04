from django.contrib import admin
from .models import Asset, Asset_Type

# Register your models here.
admin.site.register(Asset)

class Asset_Type_Admin(admin.ModelAdmin):
    fieldsets = [
    ('Overview', {'fields':['name']}),
    ]

admin.site.register(Asset_Type,Asset_Type_Admin)
