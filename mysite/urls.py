"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.webpage,name='webpage'),
    path('bikes/',views.bikes,name='bikes'),
    path('contact/',views.contact,name='contact'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('form/',views.form,name='form'),
    path('result/',views.result,name='result'),
    path('bajaj/',views.bajaj,name='bajaj'),
    path('tvs/',views.tvs,name='tvs'),
     path('hero/',views.hero,name='hero'),
        path('honda/',views.honda,name='honda'),
         path('suzuki/',views.suzuki,name='suzuki'),
         path('royalenfield/',views.royalenfield,name='royalenfield'),
         path('mahindra/',views.mahindra,name='mahindra'),
         path('yamaha/',views.yamaha,name='yamaha'),
        

    
    

]
