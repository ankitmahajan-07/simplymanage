"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login$', views.log_in, name='login'),
    url(r'^Dashboard$', views.Dashboard, name='Dashboard'),
    url(r'^logout$', views.logout, name='logout'),
    path('courses', views.courses, name='courses'),
    path('forgot', views.forgot, name='forgot'),
    path('students', views.students, name='students'),
    path('admission', views.admission, name='admission'),
    path('receipt', views.receipt, name='receipt'),
    path('rec_book', views.rec_book, name='receipt_book'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('enq_book', views.enq_book, name='enquiry_book'),

]
