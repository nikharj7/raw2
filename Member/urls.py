from django.urls import path, include
from Member.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', Member, name='Member'),
    path('Member_Dashboard', Member_Dashboard, name='Member_Dashboard'),
    path('Member_Profile', Member_Profile, name='Member_Profile'),
    path('Add_College_or_University', Add_College_or_University, name='Add_College_or_University'),
    path('College_University_List', College_University_List, name='College_University_List'),
    path('Student_Enroll', Student_Enroll, name='Student_Enroll'),
    path('Member_Notifications', Member_Notifications, name='Member_Notifications'),
    path('Member_Inbox', Member_Inbox, name='Member_Inbox'),
    path('Member_Account_Settings', Member_Account_Settings, name='Member_Account_Settings'),
    path('Member_logout', handleLogout, name='handleLogout'),
    path('Member_signup', Member_signup, name='Member_signup'),
    path('Member_login', Member_login, name='Member_login'),
    path('Success', Success, name='Success'),
    path('log', handleLogin, name='handleLogin'),
    path('profile_update', profile_update, name='profile_update'),
    path('student_list/<int:id>/', student_list, name='student_list'),
    path('Pin_Code_availiblity', Pin_Code_availiblity, name='Pin_Code_availiblity' ),
    path('search', search, name='search' ),







   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)