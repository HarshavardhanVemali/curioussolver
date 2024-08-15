from django.contrib import admin
from django.urls import path
from curioussolverapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contactus/',views.contactus,name='contactus'),
    path('aboutus/',views.aboutus,name='aboutus'),
]
