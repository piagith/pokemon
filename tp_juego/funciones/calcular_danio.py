import random
from funciones.calcular_efectividad import calcular_efectividad

#Calcula el daño de un ataque basado en los tipos y muestra su efectividad
def calcular_danio(ataque: str, tipo_atacante: str, tipo_oponente: str) -> tuple:

    efectividad, mensaje_de_efectividad = calcular_efectividad(tipo_atacante, tipo_oponente)
    danio = random.randint(20, 40) * efectividad
    return danio, mensaje_de_efectividad