from xml.etree.ElementInclude import include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.userlist, name='registeruser'),
    path('userlist/',views.userlist,name='userlist'),
    path('useradd/',views.useradd,name='useradd'),
    path('userdetail/<int:i>',views.userdetail,name='userdetail'),
    path('userdelete/<int:i>',views.userdelete,name='userdelete'),
    path('useredit/<int:i>',views.useredit,name='useredit'),
]