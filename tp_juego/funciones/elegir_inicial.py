from funciones.crear_pokemon import crear_pokemon
from funciones.crear_ataques import crear_ataques

#Permite al jugador elegir su Pokémon inicial
def elegir_pokemon_inicial() -> dict:
    """ 
    Pemite al jugador elegir su pokemon inicial: 
    Charmander, Squirtle o Bulbasaur
    
    Return:
        (str): El pokemón elegido
    """
    # Diccionario de Pokémon disponibles
    pokemones = {
        "1": {
            "nombre": "Charmander",
            "tipo" : "Fuego",
            "ataques": crear_ataques("Fuego")
        },
        "2": {
            "nombre": "Squirtle",
            "tipo" : "Agua",
            "ataques": crear_ataques("Agua")
        },
        "3": {
            "nombre": "Bulbasaur",
            "tipo" : "Planta",
            "ataques": crear_ataques("Planta")
        }
    }
    
    print("Elige tu Pokémon inicial:")
    
    # Mostrar todos los Pokémon disponibles para elegir
    for opcion, pokemon in pokemones.items():
        print(f"{opcion}: {pokemon['nombre']} (Tipo: {pokemon['tipo']})")
    
    # Validar la opción del jugador
    opcion = input("Elige 1, 2 o 3: ")
    while opcion not in pokemones:
        opcion = input("Opción inválida. Elige 1, 2 o 3: ")

    # Obtener el Pokémon elegido usando la opción validada
    pokemon_elegido = pokemones[opcion]
    
    # Crear el diccionario completo del Pokémon con HP
    pokemon_elegido = crear_pokemon(pokemon_elegido["nombre"], pokemon_elegido["tipo"], pokemon_elegido["ataques"])
    
    print(f"Has elegido a {pokemon_elegido['nombre']}")

    # Imprimir los ataques del pokemon
    # "str".join():  Es un método de cadenas que se usa para unir los elementos de una lista (o cualquier iterable) en una sola cadena, usando el valor dentro de la cadena de la cual se llama el método como separador.
    # Los elementos de la lista de ataques estarán separados por una coma y un espacio cuando los unamos.

    print(f"Sus ataques son: {', '.join(pokemon_elegido['ataques'])}")
    
    return pokemon_elegido

    """ 
    explicacion...


    El método .items() de un diccionario devuelve una lista de tuplas. Cada tupla contiene un par clave-valor. En este caso, las claves son "1", "2" y "3" (las opciones para elegir), y los valores son los diccionarios correspondientes a cada Pokémon.

    El resultado de pokemones.items() sería algo como esto:

    python
    Copiar código
    [("1", {"nombre": "Charmander", "tipo": "Fuego", "ataques": [...] }),
    ("2", {"nombre": "Squirtle", "tipo": "Agua", "ataques": [...] }),
    ("3", {"nombre": "Bulbasaur", "tipo": "Planta", "ataques": [...] })]
    Paso 2: for opcion, pokemon in pokemones.items():
    Este es un bucle for que recorre cada tupla en la lista que devuelve pokemones.items().

    opcion: Esta es la clave del diccionario. En este caso, se refiere a las opciones de elección ("1", "2" o "3").
    pokemon: Este es el valor asociado a cada clave, es decir, el diccionario que contiene los detalles del Pokémon (nombre, tipo, ataques).
    Por lo tanto, en cada iteración del bucle, las variables opcion y pokemon tomarán un valor diferente, como por ejemplo:

    En la primera iteración: opcion = "1", pokemon = {"nombre": "Charmander", "tipo": "Fuego", "ataques": [...]}.
    En la segunda iteración: opcion = "2", pokemon = {"nombre": "Squirtle", "tipo": "Agua", "ataques": [...]}.
    En la tercera iteración: opcion = "3", pokemon = {"nombre": "Bulbasaur", "tipo": "Planta", "ataques": [...]}.


    """