from django.contrib import admin
from .models import Blackcoffer

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class StudentResource(resources.ModelResource):
   class Meta:
      model = Blackcoffer
      
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource
   list_display = [f.name for f in Blackcoffer._meta.fields]
admin.site.register(Blackcoffer,StudentAdmin)   
    