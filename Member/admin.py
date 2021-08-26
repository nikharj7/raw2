from django.contrib import admin
from .models import Add_College_and_University, member
from import_export.admin import ImportExportModelAdmin
from Notification.models import *

class NotificationInlineAdmin(admin.TabularInline):
  model = Notification

class MemberAdmin(admin.ModelAdmin):
  fieldsets = (
      ('Personal Info', {
          'fields': ('user', 'profile', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'primary_phone', 'secondry_phone', 'birth_date', 'Terms_and_Conditions',)
      }),

      ('Package Info', {
          'fields': ('Paid', 'amount', 'payment_id', 'pin_code', 'package', 'document')
      }),

      ('other Info', {
          'fields': ('address_1', 'address_2', 'city', 'state', 'Country',)
      }),
  )
  search_fields = ['pin_code']

admin.site.register(member, MemberAdmin)

class Add_College_and_UniversityAdmin(admin.ModelAdmin):
  fieldsets = (
      ('College or University Info', {
          'fields': ('user', 'Profile_Picture', 'College_or_University_Name', 'Course', 'Stream', 'City', 'Pin_Code', 'slug')
      }),
   )
admin.site.register(Add_College_and_University, Add_College_and_UniversityAdmin)