from django.urls import path
from si_app import views

app_name = 'si_app'

urlpatterns = [
    path('algoritmos/',views.algo,name="algo"),
    path('arquitetura/',views.arq,name="arq"),
    path('inglês/',views.ing,name="ing"),
    path('projetos/',views.proj,name="proj"),
    path('monitoria/',views.moni,name="moni"),
    path('quemsou/',views.quemsou,name="quemsou"),
]
