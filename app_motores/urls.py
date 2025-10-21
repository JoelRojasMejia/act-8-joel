from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_motor, name='ver_motor'),
    path('agregar/', views.agregar_motor, name='agregar_motor'),
    path('editar/<int:id>/', views.editar_motor, name='editar_motor'),
    path('borrar/<int:id>/', views.borrar_motor, name='borrar_motor'),
]
