from django.contrib import admin
from main import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(models.RegisterVehicle)
class regvehicle(ImportExportModelAdmin):
    pass
@admin.register(models.BookVehicle)
class bookveh(ImportExportModelAdmin):
    pass
@admin.register(models.BulkOrder)
class bulkord(ImportExportModelAdmin):
    pass
@admin.register(models.Trip)
class tripdetail(ImportExportModelAdmin):
    pass
