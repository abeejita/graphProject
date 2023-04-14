from django.urls import include, path
from . import views

urlpatterns = [
    path('grafica',views.grafica,name='grafica'),
    path('datosGrafica',views.datosGrafica,name='datosGrafica'),
    path('grafica',views.grafica,name='grafica'),
]