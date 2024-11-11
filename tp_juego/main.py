# Funciones que imprimen información
from funciones.mostrar_opciones import mostrar_menu_opciones
from funciones.mostrar_reglas import mostrar_reglas
from funciones.mostrar_efectividades import mostrar_efectividad_de_tipos

# Funciones para jugar el juego
from funciones.crear_pokemon import crear_pokemon
from funciones.crear_ataques import crear_ataques
from funciones.elegir_inicial import elegir_pokemon_inicial
from funciones.elegir_oponente import elegir_oponente
from funciones.calcular_danio import calcular_danio
from funciones.calcular_efectividad import calcular_efectividad
from funciones.batalla import batalla

# Aquí comienza el juego
if __name__ == "__main__":
    while True:
        mostrar_menu_opciones()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_reglas()
        elif opcion == "2":
            mostrar_efectividad_de_tipos()
        elif opcion == "3":
            # Elegir el Pokémon inicial y oponente
            pokemon_jugador = elegir_pokemon_inicial()
            pokemon_oponente = elegir_oponente()
            
            # Comenzar la batalla
            batalla(pokemon_jugador, pokemon_oponente)
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break  # Sale del juego
        else:
            print("Opción inválida, por favor elige una opción válida.")