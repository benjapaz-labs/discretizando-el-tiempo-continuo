from django.contrib import admin
from django.urls import path
from backend.views import listar_personajes, seleccionar_personaje, index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),                                           # Página Principal (Frontend)
    path('api/personajes/', listar_personajes, name='listar_personajes'),        # Endpoint GET
    path('api/seleccionar/', seleccionar_personaje, name='seleccionar_personaje'), # Endpoint POST
]