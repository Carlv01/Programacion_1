class rectangulo:
    # constructor de la clase.  Se ejecuta
    # cuando la instanciamos
    def __init__(self, altura, ancho):
        print("Instanciando esta clase")

        # Atributos
        self.altura = altura
        self.ancho = ancho

        # Metodos
    def muestraElAncho(self):
        print("el ancho del rectangulo es:", self.ancho)

    def muestraLaAltura(self):
        print("la altura del rectangulo es:", self.altura)

    def calculaLaSuperficie(self):
        print(f"La superficie del rectanfulo es:",self.altura*self.ancho)

rectangulo1 = rectangulo(12, 3)
rectangulo1.muestraElAncho()

rectangulo2 = rectangulo(4, 9)
rectangulo2.muestraLaAltura()

rectangulo3 = rectangulo(5, 5)
rectangulo3.calculaLaSuperficie()
print("")

class triangulo:
    #constructor
    def __init__(self,altura,base):
       #atriutos
        self.altura = altura
        self.base = base
       #Metodos
    def muestraLaBase(self):
        print("La base del triángulo es:", self.base)

    def muestraLaAltura(self):
        print("la altura del triángulo es:", self.altura)

    def calculaElArea(self):
        print("EL área del triángulo es:",(self.altura*self.base)/2)

triangulo1 = triangulo(5, 5)
triangulo1.muestraLaAltura()
triangulo1.muestraLaBase()
triangulo1.calculaElArea()
print("")

triangulo2 = triangulo(10, 8)
triangulo2.muestraLaAltura()
triangulo2.muestraLaBase()
triangulo2.calculaElArea()