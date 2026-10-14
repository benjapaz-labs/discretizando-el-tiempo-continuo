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
            personaje_nombre = data.get('nombre')
            
            # Aquí puedes procesar la lógica de selección o guardarla
            print(f"¡Personaje seleccionado con éxito! ID: {personaje_id}, Nombre: {personaje_nombre}")
            
            return JsonResponse({
                'status': 'success',
                'mensaje': f'Personaje {personaje_nombre} seleccionado correctamente.'
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'mensaje': str(e)}, status=400)
            
    return JsonResponse({'error': 'Método no permitido'}, status=405)
# Create your views here.
