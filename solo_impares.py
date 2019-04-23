#------------------------------------------ EJERCICIO 5 solo_impares.py


numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio"))
i=1
while i<= numero_ingresado:
    if i%2!=0:
        print("soy impar: {}".format(i))
    i +=1 