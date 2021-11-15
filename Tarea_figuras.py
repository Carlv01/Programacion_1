
class FigurasGeometricas():
    def __init__(self,fig):
        self.figura = fig

    def describirForma(self,):
        print("Qué figura soy?")

class rectangulo(FigurasGeometricas):
    def describirForma(self):
        super().describirForma()
        print("Soy un",self.figura,"y Tengo 4 lados ")

class triangulo(FigurasGeometricas):
    def describirForma(self):
        super().describirForma()
        print("Soy un", self.figura, "y Tengo 3 lados")

class cuadrado(FigurasGeometricas):
    def describirForma(self):
        super().describirForma()
        print("Soy un", self.figura, "y Tengo 4 lados iguales")

class circulo(FigurasGeometricas):
    def describirForma(self):
        super().describirForma()
        print("Soy un", self.figura, "y no Tengo lados")

figura1= rectangulo("rectángulo")
figura1.describirForma()
print()
figura2= triangulo("Triángulo")
figura2.describirForma()
print()
figura3= cuadrado("Cuadrado")
figura3.describirForma()
print()
figura4= circulo("Círculo")
figura4.describirForma()