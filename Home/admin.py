from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# from import_export.admin import ImportExportModelAdmin
# # Register your models here.


class StreamAdmin(ImportExportModelAdmin):
	pass
admin.site.register(Streams, StreamAdmin )

class CourseAdmin(ImportExportModelAdmin):
	pass
admin.site.register(Courses, CourseAdmin)


class StateAdmin(ImportExportModelAdmin):
	pass
admin.site.register(State, StateAdmin)

class Pin_CodeAdmin(ImportExportModelAdmin):
	pass
admin.site.register(Pin_Code, Pin_CodeAdmin)


admin.site.register(Education)
admin.site.register(Sport)
admin.site.register(Performing_Art)