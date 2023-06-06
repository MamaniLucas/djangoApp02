#urls oi urls
from django.urls import path
from . import views
app_name = 'encuesta'


urlpatterns=[
   # path('', views.index, name ='index'),
    path('', views.calcular, name ='calcular'),
    
    #path('enviar', views.enviar, name='enviar'),
    path('calcular', views.calcular, name='calcular'),
    
]
