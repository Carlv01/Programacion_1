'''Ejercicio propuesto 1: Escribir un programa en python que calcule e imprima en pantalla
la superficie de un triángulo en función de la base y la altura (S = 1/2 Base × Altura).
Los valores son introducidos por el usr.'''

print("Bienvenido al programa trigonométrico 1")
print("Evaluaremos el area de un triangulo")
print("Por favor ingrese los siguientes datos")

num1 = float(input("Inserte valor de la base:"))
num2 = float(input("Inserte valor de la altura :"))

if num1>=0 and num2>=0:
    area = (num1 * num2)/2
    print(f"El area o superficie del triangulo es de:{area} ")
else:
    print("Valores incorrectos, por favor intente de nuevo")


