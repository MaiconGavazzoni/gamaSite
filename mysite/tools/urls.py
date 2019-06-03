from django.urls import path
from .views import hss, metalDuro

app_name = 'tools'

urlpatterns = [

    path('tabela/hss', hss, name='hss'),
    path('tabela/metalDuro', metalDuro, name='metalDuro'),

]