from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_registros, name='lista'),
    path('crear_voluntario/', views.crear_voluntario, name='crear_voluntario'),
    path("crear_evento/", views.crear_evento, name="crear_evento" ),
    path('actualizar_voluntario/<int:pk>/', views.actualizar_voluntario, name='actualizar_voluntario'),
    path('actualizar_evento/<int:pk>/', views.actualizar_evento, name='actualizar_evento'),
    path('eliminar_voluntario/<int:pk>/', views.eliminar_voluntario, name='eliminar_voluntario'),
    path('eliminar_evento/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),
    path('detalle_voluntario/<int:pk>/', views.detalle_voluntario, name='detalle_voluntario'),
    path('detalle_evento/<int:pk>/', views.detalle_evento, name='detalle_evento'),  
]   
