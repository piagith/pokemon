#Muestra las debilidades y fortalezas de cada tipo
def mostrar_efectividad_de_tipos() -> None:
    """ Muestra la efectividad de cada tipo de Pokemón """

    debilidades = """ 
    DEBILIDADES Y FORTALEZAS DE CADA TIPO:
    
    FUEGO: Débil contra el Agua <--> Fuerte contra el Planta
    AGUA: Débil contra el Eléctrico/Planta <--> Fuerte contra el Fuego
    PLANTA: Débil contra el Fuego <--> Fuerte contra el Agua
    ELECTRICO: Débil contra el Tierra <--> Fuerte contra el Agua
    """
    
    print(debilidades)