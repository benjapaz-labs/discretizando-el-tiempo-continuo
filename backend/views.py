import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Personaje

def listar_personajes(request):
    """Endpoint GET para listar todos los personajes con su ruta de imagen asegurada."""
    try:
        personajes = Personaje.objects.all()
        data = []
        for p in personajes:
            # Obtener la URL de la imagen de forma segura
            imagen_url = p.imagen.url if p.imagen and hasattr(p.imagen, 'url') else str(p.imagen)
            if not imagen_url.startswith('/'):
                imagen_url = '/' + imagen_url
                
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
    """Endpoint POST con validaciones estrictas de tipo, existencia y formato."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validación clave: el JSON debe ser un objeto/diccionario (no una lista ni null)
            if not isinstance(data, dict):
                return JsonResponse({'status': 'error', 'mensaje': 'El cuerpo de la petición debe ser un objeto JSON.'}, status=400)
                
            personaje_id = data.get('id')
            
            if personaje_id is None:
                return JsonResponse({'status': 'error', 'mensaje': 'ID no proporcionado.'}, status=400)
                
            # Forzar conversión a entero para atrapar letras o símbolos
            personaje_id = int(personaje_id)
            
            # Validar que el personaje exista en la base de datos
            personaje = Personaje.objects.get(id=personaje_id)
            
            return JsonResponse({
                'status': 'success',
                'mensaje': f'¡Éxito! Personaje {personaje.nombre} seleccionado correctamente.'
            }, status=200)
            
        except ValueError:
            return JsonResponse({'status': 'error', 'mensaje': 'ID inválido (debe ser un número entero).'}, status=400)
        except Personaje.DoesNotExist:
            return JsonResponse({'status': 'error', 'mensaje': 'El personaje seleccionado no existe en la base de datos.'}, status=404)
        except (json.JSONDecodeError, TypeError):
            return JsonResponse({'status': 'error', 'mensaje': 'Formato JSON inválido.'}, status=400)
            
    return JsonResponse({'status': 'error', 'mensaje': 'Método no permitido'}, status=405)

from django.shortcuts import render

def index_view(request):
    """Vista principal que renderiza index.html"""
    return render(request, 'index.html')