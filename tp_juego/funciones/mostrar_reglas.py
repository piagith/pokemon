#Muestra las reglas del juego
def mostrar_reglas() -> None:
    """ 
    Muestra las reglas del juego
    """

    reglas = """
    REGLAS DEL JUEGO:
    
    1) El jugador deberá elegir un Pokémon inicial para jugar:
    * Charmander: tipo Fuego
    * Squirtle: tipo Agua
    * Bulbasaur: Tipo Planta
    
    2) Se jugará contra un oponente aleatorio que puede tener cualquiera de los siguientes pokemones iniciales:
    * Cyndaquil: tipo Fuego
    * Totodile: tipo Agua
    * Chikorita: tipo Planta
    * Pikachu: tipo Eléctrico
    
    3) Acciones: El jugador puede elegir entre atacar.
    
    4) Turnos: El jugador y el oponente se turnan para realizar ataques hasta que un Pokémon sea derrotado.
    """
    print(reglas)