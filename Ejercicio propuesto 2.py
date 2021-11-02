'''Ejercicio propuesto 2: Calcular y visualizar la longitud de la circunferencia\
 y el área de un círculo de radio dado.'''

import math

print("Bienvenido al programa trigonométrico 2")
print("Evaluaremos la longitud de una circunferencia y el área de un círculo")

radio = float(input("\nInserte valor del radio:"))
if radio>=0:
    area = math.pi * radio**2
    longitud = 2 * math.pi * radio
    print(f"EL área del círculo es: {area:.2f}")
    print(f"La longitud de la circunferencia es: {longitud:.2f}")
else:
    print("Valor incorrecto, por favor intente de nuevo")