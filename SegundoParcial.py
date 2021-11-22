'''Segundo parcial:
 Un sistema de control de documentos de un Registro Publico debe ingresar y clasificar registros muy antiguos de Actas de Nacimiento y Defuncion.
 Le es solicitado crear las Clases para el sistema implementando los atributos propios para cada tipo de documento.
 Como este desarrollo se usara para el resto de documentos de ese registro publico, es imperativo que desarrolle una clase Base 'Documentos'
 de las que heradaran los de 'Nacimiento' y 'Defuncion'. Su desarrollo debe permitir el ingreso de los datos básicos del documento así como
 los datos y acciones particulares de c/u. Por temas de seguridad, el acceso a algunos atributos de la Clase debe ser privado,
  por lo que necesitará implementar los mecanismos adecuados para el ingreso de los datos. Es de suma importancia que considere:

Fecha de Expedición. El registro publico empezo a digitalizar sus documentos desde el año 2001, por lo que, los documentos posteriores
a esta fecha no deben ser incluidos.

La implementacion correcta del metodo 'MostrarFechaDelRegistro', que cambiara el mensaje de:"Nacido en fecha:xxxx"
por "Fallecido en Fecha:xxx" y viceversa, segun corresponda.

La Clase solicitada debe ser instanciada y sus metodos invocados para verificar su ejecución.'''



from abc import(ABC, abstractmethod)

class Documento(ABC):
    def __init__(self,nombre,apellidos,sexo):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__sexo = sexo


    @abstractmethod
    def MostrarFechaDelRegistro(self):
         pass

    def MostrarDatosDeLaPersona(self):
        print("La persona:", self.__nombre, self.__apellidos, "De sexo", self.__sexo)





class Nacimiento(Documento):
    def MostrarFechaDelRegistro(self):
        print(" Tiene como fecha de registro del acta de nacimiento, en el año", self.__Fnacimiento)

    def IngresarFechaDeNacimiento(self,Fnacimiento):
        if Fnacimiento > 2001:
            print("El registro publico empezo a digitalizar sus documentos a partir del año 2001, por lo que su documento no se encuentra digitalizado")
            print("Por favor ingrese la fecha adecuada posterior al 2001")
        elif  Fnacimiento <= 2001:
                self.__Fnacimiento = Fnacimiento


class Defuncion(Documento):

    def IngresarFechaDeDefuncion(self,Fdefuncion):
        if Fdefuncion > 2001:
            print("El registro publico empezo a digitalizar sus documentos a partir del año 2001, por lo que su documento no se encuentra digitalizado")
            print("Por favor ingrese la fecha adecuada posterior al 2001")
        elif Fdefuncion <= 2001:
                self.__Fdefuncion = Fdefuncion


    def MostrarFechaDelRegistro(self):
        print("Tiene como fecha de registro del acta de defuncion(fallecimiento), en el año", self.__Fdefuncion)







print("Bienvenido al Registro Público")
print("Ingrese los datos de la persona")
persona1 = Nacimiento("Carlos","vargas Rivas","Masculino")
persona1.MostrarDatosDeLaPersona()
persona1.IngresarFechaDeNacimiento(2000)
persona1.MostrarFechaDelRegistro()

print()

print("Bienvenido al Registro Público")
print("Ingrese los datos de la persona")
persona2 = Defuncion("Jose","Perez Mendoza","Masculino")
persona2.MostrarDatosDeLaPersona()
persona2.IngresarFechaDeDefuncion(1995)
persona2.MostrarFechaDelRegistro()







