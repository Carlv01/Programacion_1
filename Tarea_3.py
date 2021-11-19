class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self. modelo = modelo
        self.anio = anio
        print("Vehiculo Creado")

    def encender(self):
        print("Estoy listo para llevarte")

    def arrancar(self):
        print("raaahh rahh!!")


class Automovil(Vehiculo):  # herencia simple: Automovil extiende a Vehiculo
    __litrosGasolina = 0
    transmisionManual = True

    def encender(self):  # ejemplo de Polimorfismo - overriding
        print("Listo para llevarte en este", self.modelo)

    def arrancar(self):
        print("Comienzo a rodar!!!")

    def tocarCorneta(self):
        print("beep beep!")

    def echarGasolina(self, vlitros):  # Encapsulamiento - esto es un setter
        if vlitros <= 1:
            print("con un solo litro, no llegas a ninguna parte")
        else:
            if vlitros>=0 and vlitros<=40:
                print("Echando gasolina para poder rodar, recuerda el maximo es de 40 litros")
                self.__litrosGasolina = vlitros
            else:
                print("No puedes echar esa cantidad, el maximo es de 40 litros")

    def cuantaGasolinaHay(self):  # Encapsulamiento - esto es un getter
        print("Ud. tiene:", self.__litrosGasolina, "litros de Gasolina")

class moto(Vehiculo):
    __litrosGasolina = 0
    __ligaDeFrenos = 0
    def __init__(self,marca, modelo, anio,peso):
        super().__init__(marca,modelo,anio)
        self.__peso = peso


    def datosdelamoto(self):
        print("PREPARATE!!! porque conduces una moto",self.marca,"modelo",self.modelo,"año",self.anio,"con un peso de",self.__peso,"kg")

    def arrancar(self):
        if self.__litrosGasolina >=2 and self.__ligaDeFrenos >=51:
            print("Estamos listos! Empiezo avanzar... ¡SUJÉTATE BIEN!")
        else:
            print("chequea tu gasolina o liga de frenos, puede que no tengas suficiente")


    def echarGasolina(self,vlitros):  # Encapsulamiento - esto es un setter
        if vlitros <= 1:
            print("con un solo litro, no llegas a ninguna parte")
        else:
            if vlitros>=2 and vlitros<=18:
                print("Echando gasolina para poder rodar, recuerda la capacidad va desde 2 a 18 litros")
                self.__litrosGasolina = vlitros
            else:
                print("No puedes echar esa cantidad, el maximo es de 18 litros")

    def cuantaGasolinaHay(self):  # Encapsulamiento - esto es un getter
        print("Revisando su gasolina... Ud. tiene:", self.__litrosGasolina, "litros de Gasolina")

    def cantidadDeLigaFreno(self):
        print("Revisando su liga de frenos... Ud. tiene:", self.__ligaDeFrenos, "ml de liga de frenos")

    def echarLigaFreno(self,vliga):
        if vliga <=50:
            print("No tienes suficiente liga de frenos. Por favor échale y evita una desgracia en tu vida ")
        else:
            if vliga>=51 and vliga<=1000:
                print("Echando liga de frenos. Mejorará los frenos de tu vehiculo. Recuerda la capacidad va de 50 a 1000 ml")
                self.__ligaDeFrenos = vliga
            else:
                print("No puedes echar esa cantidad, el maximo es de 1000 ml")





moto1 = moto("DUCATI","Superrllegera V4",2021,159)
moto1.datosdelamoto()
moto1.encender()
moto1.cuantaGasolinaHay()
moto1.echarGasolina(10)
moto1.cuantaGasolinaHay()
moto1.cantidadDeLigaFreno()
moto1.echarLigaFreno(51)
moto1.cantidadDeLigaFreno()
moto1.arrancar()

print()
coche2 = Automovil("ford","GT500",2015)
coche2.encender()
coche2.cuantaGasolinaHay()
coche2.echarGasolina(40)
coche2.cuantaGasolinaHay()
coche2.arrancar()









# Ejercicio 5pts.
# Instancie otro objeto.
# 1.- Haga herencia de la clase padre
# 2.- Necesito mas especificidad en la administracion del atributo __galonesGasolina
# 3.- Defina un nvo. atributo protegido.  Defina la administracion del acceso a ese atributo.
# 4.- Haga overriding del metodo arrancar.


# instanciando la clase Vehiculo-Automovil
'''miCarro = Automovil("Chevrolet", "Aveo", "2015")
miCarro.encender()
miCarro.tocarCorneta()
miCarro.cuantaGasolinaHay()
miCarro.echarGasolina(100)
miCarro.cuantaGasolinaHay()'''
