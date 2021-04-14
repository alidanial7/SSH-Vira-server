from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Cook)
admin.site.register(models.Food)
admin.site.register(models.Chef)
admin.site.register(models.Distributor)
admin.site.register(models.Distribution)
admin.site.register(models.Meal)
admin.site.register(models.Report)
