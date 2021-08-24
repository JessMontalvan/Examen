from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('nuevoreg', views.CreateUser.as_view(), name='nuevoreg'),
    path('lista', views.listUser, name='lista'),
    url(r'^editar/(?P<pk>\d+)/$', views.EditUser.as_view(), name="editar"),    
    path('eliminar/<int:id>/', views.deleteUser, name='eliminar'),

]
