import random
from funciones.crear_pokemon import crear_pokemon
from funciones.crear_ataques import crear_ataques

#Elige un oponente aleatorio para el jugador
def elegir_oponente() -> dict:
    
    oponentes = {
        "1": {
            "nombre": "Cyndaquil",
            "tipo": "Fuego",
            "ataques": crear_ataques("Fuego")
        },
        "2": {
            "nombre": "Totodile",
            "tipo": "Agua",
            "ataques": crear_ataques("Agua")
        },
        "3": {
            "nombre": "Chikorita",
            "tipo": "Planta",
            "ataques": crear_ataques("Planta")
        },
        "4": {
            "nombre": "Pikachu",
            "tipo": "Electrico",
            "ataques": crear_ataques("Electrico")
        }
    }
    
    # Elegir una opción aleatoria de entre las claves del diccionario
     # Elegir una opción aleatoria de entre las claves del diccionario
    # explicación ----->
    # oponentes.keys(): es un objeto de tipo dict_keys, que se ve como una lista, pero no es una lista propiamente dicha. Keys() es un método de los diccionarios en Python que devuelve una vista de todas las claves en el diccionario
    # a función list() convierte el objeto dict_keys en una lista estándar de Python
    # list(oponentes.keys()): ['1', '2', '3', '4']
    opcion = random.choice(list(oponentes.keys()))
    
    # Obtener el oponente elegido
    oponente_elegido = oponentes[opcion]
    
    # Crear el diccionario completo del oponente con HP
    oponente_elegido = crear_pokemon(oponente_elegido["nombre"], oponente_elegido["tipo"], oponente_elegido["ataques"])
    
    print(f"Tu oponente es: {oponente_elegido['nombre']} (Tipo: {oponente_elegido['tipo']})")
    
    return oponente_elegido