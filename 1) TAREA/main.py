#Desarrollo de un Algoritmo Para la Generación de Rimas
import random

# Lista de posibles frases o palabras
frases = [
    "Desarrollar múltiples trabajos",
    "Me permite aumentar la eficiencia en múltiples campos",
    "para mantener la mente ocupada en múltiples lados",
    "es fundamental mantener a vista orientada en todos lados"
]

#Función para extraer los  últimos tres caracteres

def extraer_ultimos_tres(frase):
    return frase[-3:]

#Procedo a crear un diccionario para las diferentes rimas
rimas = {}
for frase in frases:
    clave = extraer_ultimos_tres(frase)
    if clave in rimas:
        rimas[clave].append(frase)
    else:
        rimas[clave] = [frase]

# Asignar estado d e exploración aleatoria
explorados = {frase: random.choice([True, False]) for frase in frases}

#Mostrar Resultados
for clave, grupo in rimas.items():
    print(f"Rima '{clave}':")
    for frase in grupo:
        estado = "Explorado " if explorados[frase] else "No explorado"
        print(f"-{frase}->{estado}")
    print()
    