'''Evaluacion 1 : A) Los valores (en enteros) de temperatura de varias calderas se registran en una lista que le es proporcionada. vTemperaturas
= = [36, 42, 57, 58, 07, 45, 26, 35, 83, 56, 57, 97, 28, 115, 53, 35, 99, 62, 78, 29, 98, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 104, 58, 512, 24, 92, 89, 67, 53, 81, 79, 83, 81, 44, 132, 77, 98, 73, 57]
Escriba un programa en python 3 que imprima solo los números pares de la lista y/o el mensaje: "URGENTE! La temperatura es mayor a 100 grados" si uno de los valores (par o impar) es mayor que 100 en la secuencia. Haga uso de una función que ayude a mostrar esta salida de forma más legible (como la vimos en clase).

Ponderación: Ejecución correcta del programa: 5 pts. Uso correcto de variables: 3 pts. Uso correcto de la sentencia for: 5 pts. Uso correcto de la sentencia if: 5 pts. Uso de la función: 2 pts.

Tiene hasta las 3:30pm. para subir su respuesta a su repositorio GitHub. Commits después de esta hora, no seran tomados en cuenta.'''

def Npar(i):
    print(f"la temperatura {i} es par")
def N100(i):
    print(f"{i}'URGENTE! La temperatura es mayor a 100 grados' ")


vTemperaturas = [36, 42, 57, 58, 7, 45, 26, 35, 83, 56, 57, 97, 28, 115, 53, 35, 99, 62, 78, 29, 98, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 104,58, 512, 24, 92, 89, 67, 53, 81, 79, 83, 81, 44, 132, 77, 98, 73, 57]
for i in vTemperaturas:
    if i%2==0 or i>=100:
        if i%2==0 and i<100:
            print(f"la temperatura es igual a: {i}")
        elif i>=100:
            print(f"{i}'URGENTE! La temperatura es mayor a 100 grados'")

'''Profe intruje la funcion dentro de los condicionales pero al final de cada resultado me aparecia un none ,
 no se si esta bueno o no pero preferi no usarlo porque puede que afecte la validacion del resultado, de igual 
 forma si no entiende le puedo adjuntar una captura y me explica luego como eliminar eso para no cometerlo en 
 futuros codigos. GRACIAS!  '''