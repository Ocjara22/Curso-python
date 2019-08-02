
def depositar(saldo, cantidad):
    saldo += cantidad
    print("He depositado")
    return saldo

def girar(saldo, cantidad):
    print("he girado")

def mostrar_menu(saldo = 0):
    opcion = 1

    while  opcion != 4:
        print("Bienvenido al portal del Banco Amigo. Escoja una opción:")
        print("1. Consultar saldo")
        print("2. Hacer depósito") 
        print("3. Realizar giro")
        print("4. Salir")
        opcion = int(input(" "))

        if opcion == 1:
            print(saldo)
        elif opcion == 2:
            print("hola")
            deposito = int(input("Ingresar cantidad a depositar"))
            saldo =  depositar(saldo, deposito)
            print(saldo)
        elif opcion == 3:
            giro = int(input("Ingresar cantidad a girar"))
            girar(saldo, giro)
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.")


mostrar_menu()
