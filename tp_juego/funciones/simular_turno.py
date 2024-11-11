import random
from funciones.calcular_danio import calcular_danio

# Simula un turno de batalla (jugador u oponente)
def simular_turno(atacante: dict, defensor: dict, es_oponente: bool = False) -> str:
    """Simula un turno de batalla entre el jugador y el oponente"""
    if es_oponente:
        print(f"Es el turno de {defensor['nombre']} (¡oponente!)")
        ataque = random.choice(defensor["ataques"])  # El oponente elige un ataque aleatorio
        print(f"{defensor['nombre']} elige usar {ataque}")
    else:
        print(f"Es el turno de {atacante['nombre']} (¡tu turno!)")
        print("Elige un ataque:")
        for i, ataque in enumerate(atacante["ataques"], 1):
            print(f"{i}. {ataque}")
        
        # Validación para que el jugador elija un ataque válido
        """
        El try es donde colocamos el código que queremos ejecutar, y en el cual podría ocurrir un error (o una "excepción"). 
        Si todo el código dentro del try se ejecuta sin problemas, 
        entonces se salta el bloque except y el programa sigue su curso.
        """
        while True:
            try:
                ataque_elegido = int(input("Elige un número para el ataque: ")) - 1
                if ataque_elegido < 0 or ataque_elegido >= len(atacante["ataques"]):
                    print("Número de ataque inválido. Por favor elige un número válido.")
                else:
                    break
            except ValueError:
                print("Por favor, elige un número válido.")
        
        ataque = atacante["ataques"][ataque_elegido]
    
    # Calculamos el daño con el ataque elegido
    danio, mensaje_efectividad = calcular_danio(ataque, atacante["tipo"], defensor["tipo"])
    
    # Reducimos los puntos de vida del defensor
    defensor["hp"] -= danio
    print(f"{atacante['nombre']} usa {ataque} y causa {danio} puntos de daño a {defensor['nombre']}")
    print(f"{defensor['nombre']} tiene {defensor['hp']} hp restantes")
    print(f"El ataque fue: {mensaje_efectividad}")
    
    # Verificamos si el defensor ha sido derrotado
    if defensor["hp"] <= 0:
        return f"{defensor['nombre']} ha sido derrotado."
    
    return None  # La batalla sigue si el defensor tiene vida