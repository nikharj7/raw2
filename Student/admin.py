from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class StudentAdmin(ImportExportModelAdmin):
  pass
  # fieldsets = (
  #     ('Personal Info', {
  #         'fields': ('user', 'First_Name', 'Middle_Name', 'Last_Name', 'Gender', 'Mobile', 'Email', 'DOB',)
  #     }),
  #     ('Education info', {
  #         'fields': ('Course', 'University_Name', 'Year_Start', 'Year_End' )
  #     }),
  #     ('Address info', {
  #         'fields': ('Address_1', 'Address_2', 'City', 'State', 'Country', 'Pin_Code' )
  #     }),
  #     ('Social Profile', {
  #         'fields': ('Facebook_Profile', 'Linkedin', 'Twitter_Profile' )
  #     }),
  #  )
admin.site.register(student, StudentAdmin)


admin.site.register(New_Student)