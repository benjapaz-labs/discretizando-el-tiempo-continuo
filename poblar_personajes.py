import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'juego.settings')
django.setup()

from backend.models import Personaje

def poblar():
    personajes_data = [
        {
            "nombre": "Sram",
            "x": 50,
            "y": 50,
            "velocidad": 30,
            "imagen": "sram.jpg"
        },
        {
            "nombre": "Feca",
            "x": 100,
            "y": 100,
            "velocidad": 40,
            "imagen": "feca.jpg"
        },
        {
            "nombre": "Osa",
            "x": 150,
            "y": 150,
            "velocidad": 35,
            "imagen": "osa.jpg"
        },
    ]

    print("🚀 Iniciando población de personajes...")
    for p in personajes_data:
        personaje, created = Personaje.objects.update_or_create(
            nombre=p['nombre'],
            defaults={
                'x': p['x'],
                'y': p['y'],
                'velocidad': p['velocidad'],
                'imagen': p['imagen']
            }
        )
        if created:
            print(f"✅ Personaje creado: {personaje.nombre}")
        else:
            print(f"ℹ️ El personaje {personaje.nombre} fue actualizado con éxito.")
    print("✨ ¡Población finalizada con éxito!")

if __name__ == '__main__':
    poblar()