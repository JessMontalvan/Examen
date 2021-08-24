from django.urls import path
from django.conf.urls import url
from . import views
from .views import *


app_name = 'ticket'

urlpatterns = [
    path('', views.homepage, name='homepage'),
     path('nuevotick', views.CreateUser.as_view(), name='nuevotick'),
     path('user', views.listUser, name='user'),
     url(r'^editar/(?P<pk>\d+)/$', views.EditUser.as_view(), name="editar"),    
     path('eliminar/<int:id>/', views.deleteUser, name='eliminar'),

 ]