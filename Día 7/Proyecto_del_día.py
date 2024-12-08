from os import system
from random import randint


class Persona():

    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    #Debe imprimir los datos del cliente asi como el balance de su cuenta
    def datos_cliente(self):
        print(f'Cliente {self.nombre} {self.apellido}')
        print(f'Numero de Cuenta: {self.numero_cuenta}')
        print(f'Balance: {self.balance}')

    #Debe permitir deposita n cantidad de dinero al cliente
    def depositar(self, cantidad):
        self.balance += cantidad

    #Debe permitir retirar una n cantidad de dinero al cliente
    def retirar(self, cantidad):

        if  self.balance - cantidad < 0:
            print('Fondos insuficientes')
            self.balance + cantidad
        else:
            self.balance -= cantidad


#Funcion para crear al cliente
def crear_cliente():

    nombre = input('Dime tu nombre\n')
    apellido = input('Dime tu apellido\n')
    numero_cuenta = randint(1,10000)
    balance = 0


    nuevo_cliente = Cliente(nombre, apellido, numero_cuenta, balance)

    return nuevo_cliente

#Codigo que permita elegir si depositar, retirar o Salir

def menu():

    print('''\n\nElige alguna operacion
        [1] Depositar
        [2] Retirar
        [3] Salir''')

    op = int(input())

    return op

def main():

    mi_cliente = crear_cliente()
    print(f'\nbienvenido {mi_cliente.nombre} {mi_cliente.apellido}')

    while True:
        mi_cliente.datos_cliente()

        match menu():
            case 1:
                cantidad = int(input('Dime la cantidad a depositar\n'))
                mi_cliente.depositar(cantidad)
                pass
            case 2:
                cantidad = int(input('Dime la cantidad a retirar\n'))
                mi_cliente.retirar(cantidad)
                pass
            case 3:
                return False
        input('Presiona ENTER para continuar')
        system('cls')
main()

