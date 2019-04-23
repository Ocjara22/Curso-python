#-------------------------------------------EJERCICIO 4 solo_pares_refactor.py

numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio\n"))
i=1
while i<= numero_ingresado:
    if i%2==0:
        print("soy par: {}".format(i))
    i +=1   


numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio\n"))
i=0
while i<= numero_ingresado:
    if i%2==0:
        if  i!=0:
            print("soy par: {}".format(i))
    i +=1   

  