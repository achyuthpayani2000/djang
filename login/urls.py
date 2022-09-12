from xml.etree.ElementInclude import include

from django.urls import path

import users
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),

]