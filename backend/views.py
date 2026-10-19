import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Personaje

def listar_personajes(request):
    """Endpoint GET para listar todos los personajes asegurando la ruta estática de la imagen."""
    try:
        personajes = Personaje.objects.all()
        data = []
        for p in personajes:
            imagen_path = str(p.imagen) if p.imagen else ''
            
            if imagen_path.startswith('/'):
                imagen_path = imagen_path[1:]
                
            if not imagen_path.startswith('static/'):
                imagen_path = f"static/{imagen_path}"
                
            imagen_url = f"/{imagen_path}"
                
            data.append({
                "id": p.id,
                "nombre": p.nombre,
                "x": p.x,
                "y": p.y,
                "velocidad": p.velocidad,
                "imagen": imagen_url
            })
        return JsonResponse({"personajes": data}, status=200)
    except Exception as e:
        return JsonResponse({"status": "error", "mensaje": str(e)}, status=500)

@csrf_exempt
def seleccionar_personaje(request):
    """Endpoint POST para procesar la selección del personaje."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            if not isinstance(data, dict):
                return JsonResponse({'status': 'error', 'mensaje': 'El cuerpo debe ser un objeto JSON.'}, status=400)
                
            personaje_id = data.get('id')
            if personaje_id is None:
                return JsonResponse({'status': 'error', 'mensaje': 'ID no proporcionado.'}, status=400)
                
            personaje_id = int(personaje_id)
            personaje = Personaje.objects.get(id=personaje_id)
            
            return JsonResponse({
                'status': 'success',
                'mensaje': f'¡Personaje {personaje.nombre} seleccionado con éxito!'
            }, status=200)
            
        except ValueError:
            return JsonResponse({'status': 'error', 'mensaje': 'ID inválido.'}, status=400)
        except Personaje.DoesNotExist:
            return JsonResponse({'status': 'error', 'mensaje': 'El personaje no existe.'}, status=404)
        except (json.JSONDecodeError, TypeError):
            return JsonResponse({'status': 'error', 'mensaje': 'Formato JSON inválido.'}, status=400)
            
    return JsonResponse({'status': 'error', 'mensaje': 'Método no permitido'}, status=405)

def index_view(request):
    """Renderiza el template principal de selección."""
    return render(request, 'index.html')