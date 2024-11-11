from funciones.simular_turno import simular_turno

# Simula la batalla entre jugador/oponente
def batalla(pokemon_jugador: dict, pokemon_oponente: dict) -> None:
    print(f"La batalla comienza! {pokemon_jugador['nombre']} contra {pokemon_oponente['nombre']}")
    
    while pokemon_jugador["hp"] > 0 and pokemon_oponente["hp"] > 0:
        # El turno del jugador
        resultado = simular_turno(pokemon_jugador, pokemon_oponente, es_oponente=False)
        
        if resultado:
            print(resultado)
            print("¡Ganaste!")
            break  # Sale de la batalla si hay un ganador
        
        # El turno del oponente
        resultado = simular_turno(pokemon_oponente, pokemon_jugador, es_oponente=True)
        
        if resultado:
            print(resultado)
            print("Perdiste")
            break  # Sale de la batalla si el oponente gana