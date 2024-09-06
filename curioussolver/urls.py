from django.contrib import admin
from django.urls import path
from curioussolverapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contactus/',views.contactus,name='contactus'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('registerpage/',views.registerpage,name='registerpage'),
    path('registerform/',views.register,name='registerform'),
    path('researchpaper/',views.researchpaper,name='researchpaper'),
    path('websitedevelopment/',views.websitedevelopment,name='websitedevelopment'),
    path('patents/',views.patents,name='patents'),
    path('courses/',views.courses,name='courses'),
    path('ugprojects/',views.ugprojects,name='ugprojects'),
    path('pgprojects/',views.pgprojects,name='pgprojects'),
    path('internships/',views.internships,name='internships'),
]
