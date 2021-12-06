

class Cuenta:
    def __init__(self,nombre,sexo,edad):
        self.nombre = nombre
        self.sexo = sexo
        self.Edad = edad


    def DatosDelUsuario(self):
        print(" El usuario es:", self.nombre)
        print("Edad:", self.Edad)
        print("Sexo:", self.sexo)


    def Saldo(self,capital):
        if capital < 0:
            print(" No puede tener saldo negativo")
        elif capital >= 0:
            self.Capital = capital

    def ConsultarSaldo(self):
        print("Su saldo es:", self.Capital)

    def DepositarSaldo(self,Deposito):
        self.Capital += Deposito
        print("La cantidad depositada es de:",Deposito)

    def RetirarSaldo(self,Retiro):
        if Retiro <= self.Capital:
            self.Capital -= Retiro
            print("La cantidad retirada es de:", Retiro)
        else:
            print("No dispones de esa cantidad para retirar")

    def Intereses(self,tasa,tiempo):
        if tasa > 0 and tiempo > 0:
            self.tasa = tasa
            self.tiempo = tiempo

    def AbonoDeIntereses(self):
        InteresesAPagar = self.Capital * self.tasa * self.tiempo
        print("Los Intereses estan estructurados de la siguiente manera")
        print("La tasa es de:",self.tasa)
        print("La cantidad de meses es de:",self.tiempo)
        print("El interes a pagar es de:", InteresesAPagar)



class PlazoFijo(Cuenta):


    def AbonoDeIntereses(self):
        InteresesAPagar = self.Capital * self.tasa * self.tiempo
        bono = self.Capital * 0.10
        InteresesAPagar += bono
        print("El interes a pagar es de:", InteresesAPagar)

class CuentaDeAhorro(Cuenta):
    pass

print("Bienvenido al Banco")
Usuario1 = CuentaDeAhorro("pedro Alvarez","Hombre",45)
Usuario1.DatosDelUsuario()
Usuario1.Saldo(2000)
Usuario1.ConsultarSaldo()
Usuario1.DepositarSaldo(5000)
Usuario1.ConsultarSaldo()
Usuario1.RetirarSaldo(5000)
Usuario1.ConsultarSaldo()
Usuario1.Intereses(1.6,4)
Usuario1.AbonoDeIntereses()

Usuario2 = PlazoFijo("leo","Mujer",55)
Usuario2.DatosDelUsuario()
Usuario2.Saldo(2000)
Usuario2.Intereses(1.6,4)
Usuario2.AbonoDeIntereses()






'''    

Estuve intentando de esta manera profe pero me complique 
luego le comento de esto 




menu = [
        ['1.Consultar saldo',"anadir"],
        ['2. Depositar dinero'],
        ['3. Retirar dinero'],
        ['4. Salir']
    ]

    for x in range(4):
        print(menu[x][0])

    opcion = int(input("Introduzca una opcion:"))
    if opcion == 1:

    elif opcion == 2:
        self.Depositar()
    elif opcion == 3:
        self.RetirarDinero()
    elif opcion == 4:
        print("Ha Salido del menu Bancario")





    def RetirarDinero(self,retirar):
        retirar = int(input("Cuanto dinero desea retirar?:"))
        if retirar > self.Capital:
            print("La cantidad que desea retirar es mayor a la que tiene disponible")
        elif retirar <= self.Capital:
            saldoFinal = self.Capital - retirar
            print("Retiró",retirar)
            print("El saldo que quedó en la cuenta es de",saldoFinal)



'''
