from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# Register your models here.

admin.site.register(Member_Notification)
admin.site.register(Student_Notification)
admin.site.register(Company_Notification)



class NotificationInlineAdmin(admin.StackedInline):
  model = Notification
  
class UserAdmin(AuthUserAdmin):
	def add_view(self, *args, **kwargs):
		self.inlines = []
		return super(UserAdmin, self).add_view(*args, **kwargs)

	def change_view(self, *args, **kwargs):
		self.inlines = [NotificationInlineAdmin]
		return super(UserAdmin, self).change_view(*args, **kwargs)


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
