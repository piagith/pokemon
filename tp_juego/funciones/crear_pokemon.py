import random

#Genera un Pokémon con un nombre, tipo y ataques
def crear_pokemon(nombre: str, tipo: str, ataques: list) -> dict:
    """ Crea un Pokemón con sus respectivos atributos, asignando hp 
    aleatorio entre 100 y 120.
    
    Args:
        nombre(str): Nombres del pokemón a crear
        tipo(str): Tipo del pokemón a crear
        ataques(list): Lista de todos los ataques del pokemón a crear
        hp(int): Puntaje de vida del pokemón a crear
    
    Return:
        (dict): Retorna un diccionario con todos los atributos y sus caracteristicas
    """

    hp = random.randint(100, 120)  # HP aleatorio entre 100 y 120
    atributos = {
        "nombre": nombre,
        "tipo": tipo,
        "ataques": ataques,
        "hp": hp
    }
    return atributos