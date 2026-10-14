from django.shortcuts import render

# Vista para mostrar la página principal con el Frontend
def index_view(request):
    return render(request, 'index.html')
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Personaje

# Endpoint GET: Entrega todos los personajes disponibles (Punto 2)
def listar_personajes(request):
    if request.method == 'GET':
        personajes = list(Personaje.objects.values('id', 'nombre', 'x', 'y', 'velocidad', 'imagen'))
        return JsonResponse({'personajes': personajes}, safe=False)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Endpoint POST: Recibe la selección del personaje (Punto 3)

@csrf_exempt
def seleccionar_personaje(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            personaje_id = data.get('id')
            
            # Validar que el personaje exista en la base de datos
            personaje = Personaje.objects.get(id=personaje_id)
            
            print(f"¡Personaje seleccionado con éxito! ID: {personaje.id}, Nombre: {personaje.nombre}")
            
            return JsonResponse({
                'status': 'success',
                'mensaje': f'¡Éxito! Personaje {personaje.nombre} seleccionado correctamente.'
            }, status=200)
            
        except Personaje.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'mensaje': 'El personaje seleccionado no existe en la base de datos.'
            }, status=404)
            
        except (json.JSONDecodeError, TypeError):
            return JsonResponse({
                'status': 'error',
                'mensaje': 'Formato JSON inválido.'
            }, status=400)
            
    return JsonResponse({'status': 'error', 'mensaje': 'Método no permitido'}, status=405)