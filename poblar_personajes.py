import os
import django

# Configurar el entorno de Django (apuntando directo a settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'juego.settings')
django.setup()

from backend.models import Personaje

def crear_personajes():
    # Lista de personajes a agregar (mínimo 3, tal como pide la pauta)
    personajes_data = [
        {"nombre": "Devil", "x": 50, "y": 50, "velocidad": 30},
        {"nombre": "Auto", "x": 100, "y": 100, "velocidad": 40},
        {"nombre": "Dino", "x": 150, "y": 150, "velocidad": 35},
    ]

    for data in personajes_data:
        personaje, creado = Personaje.objects.get_or_create(
            nombre=data["nombre"],
            defaults={
                "x": data["x"],
                "y": data["y"],
                "velocidad": data["velocidad"]
            }
        )
        if creado:
            print(f"-> Personaje creado con éxito: {personaje.nombre}")
        else:
            print(f"-> El personaje '{personaje.nombre}' ya existía en la base de datos.")

if __name__ == '__main__':
    print("Iniciando la carga de personajes...")
    crear_personajes()
    print("¡Proceso finalizado!")