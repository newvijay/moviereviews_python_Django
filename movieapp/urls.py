from django.urls import path, re_path
from . import views


urlpatterns=[
    path('',views.testing,name='home'),
    path('nextpage',views.testing,name='nextpage')
]

