from django.urls import path
from galeria.views import view,view2

urlpatterns = [
    path('', view, name= 'index'),
    path('imagem/', view2, name= 'imagem'),
]