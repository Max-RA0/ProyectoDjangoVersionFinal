from django.urls import path
from . import views

urlpatterns = [
    path('', views._home, name='home'),
    path('<str:tipo>/lista_servicios/', views._lista_servicios, name='lista_servicios'),
    path('<str:tipo>/lista_asesoria/', views._lista_asesoria, name='lista_asesoria'),
    path('<str:tipo>/crear/', views._crear_servicio, name='crear_servicio'),
    path('editar_servicio/<str:tipo>/<int:pk>/', views._editar_servicio, name='editar_servicio'),
    path('eliminar_servicio/<int:pk>/', views._eliminar_servicio, name='eliminar_servicio'),
    path('search/', views.search, name='search'),
    
]

