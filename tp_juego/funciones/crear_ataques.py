def crear_ataques(tipo) -> list:
    """Genera ataques según el tipo del Pokémon.
    
    Arguments:
        tipo(str): el tipo de pokemón
    
    Return:
        (list): Lista con los ataques del tipo del pokemon
    
    """

    if tipo == "Fuego":
        return ["Lanzallamas", "Ember", "Puño fuego", "Golpe ardiente"]
    elif tipo == "Agua":
        return ["Hidrobomba", "Pistola de agua", "Surf", "Golpe acuario"]
    elif tipo == "Planta":
        return ["Rayo solar", "Hoja afilada", "Látigo cepa", "Drenaje"]
    elif tipo == "Electrico":
        return ["Rayo", "Trueno", "Impactrueno", "Puño trueno"]