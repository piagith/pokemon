#Calcula la efectividad del ataque dependiendo de los tipos
def calcular_efectividad(tipo_atacante: str, tipo_oponente: str) -> tuple:

    efectividad = 1
    mensaje_de_efectividad = "Efectivo"
    
    # Debilidades y resistencias
    if tipo_atacante == "Fuego" and tipo_oponente == "Agua":
        efectividad = 0.5
        mensaje_de_efectividad = "Poco efectivo (Fuego contra Agua)"
    elif tipo_atacante == "Fuego" and tipo_oponente == "Planta":
        efectividad = 2
        mensaje_de_efectividad = "Muy efectivo (Fuego contra Planta)"
    elif tipo_atacante == "Agua" and tipo_oponente == "Fuego":
        efectividad = 2
        mensaje_de_efectividad = "Muy efectivo (Agua contra Fuego)"
    elif tipo_atacante == "Agua" and tipo_oponente == "Planta":
        efectividad = 0.5
        mensaje_de_efectividad = "Poco efectivo (Agua contra Planta)"
    elif tipo_atacante == "Planta" and tipo_oponente == "Agua":
        efectividad = 2
        mensaje_de_efectividad = "Muy efectivo (Planta contra Agua)"
    elif tipo_atacante == "Planta" and tipo_oponente == "Fuego":
        efectividad = 0.5
        mensaje_de_efectividad = "Poco efectivo (Planta contra Fuego)"
    elif tipo_atacante == "Electrico" and tipo_oponente == "Agua":
        efectividad = 2
        mensaje_de_efectividad = "Muy efectivo (Electrico contra Agua)"
    elif tipo_atacante == "Electrico" and tipo_oponente == "Tierra":
        efectividad = 0
        mensaje_de_efectividad = "Inútil (Electrico contra Tierra)"
    
    return efectividad, mensaje_de_efectividad