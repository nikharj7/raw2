from django.urls import path, include
from Student.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', Student, name='Student'),
    path('Student_Dashboard', Student_Dashboard, name='Student_Dashboard'),
    path('Student_Profile', Student_Profile, name='Student_Profile'),
    path('Academics', Academics, name='Academics'),
    path('Area_of_Interest', Area_of_Interest, name='Area_of_Interest'),
    path('Notifications', Notifications, name='Notifications'),
    path('Inbox', Inbox, name='Inbox'),
    path('Account_Settings', Account_Settings, name='Account_Settings'),
    path('logout', handleLogout, name='handleLogout'),
    path('login', handleLogin, name='handleLogout'),
    path('search', search, name='search'),


   
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
