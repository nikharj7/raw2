from django.urls import path, include
from Company.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', Company, name='Company'),
    path('Company_Dashboard', Company_Dashboard, name='Company_Dashboard'),
    path('Company_Profile', Company_Profile, name='Company_Profile'),
    path('Internship', Internship, name='Internship'),
    path('Job', Job, name='Job'),
    path('Company_Account_Settings', Company_Account_Settings, name='Company_Account_Settings'),
    path('logout', handleLogout, name='handleLogout'),
   	path('Company_login', Company_login, name='Company_login'),
    path('register_company', register_company, name='register_company'),
    path('search', search, name='search'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
