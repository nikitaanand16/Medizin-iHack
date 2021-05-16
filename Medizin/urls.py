"""Medizin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),    
    url(r'^$',views.index,name="index"), 
    url(r'^dia/$',views.dia,name="dia"),
    url(r'^diavisual/$',views.diavisual,name="diavisual"),
    url(r'^diaresult/$',views.diaresult,name="diaresult"),
    url(r'^medical/$',views.medical,name="medical"),
    url(r'^tumor/$',views.tumor,name="tumor"),
    url(r'^tumorvisual/$',views.tumorvisual,name="tumorvisual"),
    url(r'^add/$',views.add,name="add"),
    url(r'^view/$',views.view,name="view"),
    url(r'^delete/$',views.delete,name="delete"),
    url(r'^blog/$',views.blog,name="blog"),
    url(r'^doc/$',views.doc,name="doc"),
    url(r'^patientq/$',views.patientq,name="patientq"),
    url(r'^patienthistory/$',views.patienthistory,name="patienthistory"),
    url(r'^inappropiate/$',views.inappropiate,name="inappropiate"),
    url(r'^patienta/$',views.patienta,name="patienta"),
    url(r'^reply/$',views.reply,name="reply"),
    url(r'^expert/$',views.expert,name="expert"),
    url(r'^find/$',views.find,name="find"),
    url(r'^search/$',views.search,name="search"),
    url(r'^heartvisuals/$',views.heartvisuals,name="heartvisuals"),
    url(r'^hearts/$',views.hearts,name="hearts"),
    
]