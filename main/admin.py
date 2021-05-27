from django.contrib import admin
from main import models
# Register your models here.

admin.site.register(models.RegisterVehicle)
admin.site.register(models.BookVehicle)
admin.site.register(models.BulkOrder)
admin.site.register(models.Trip)
