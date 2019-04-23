#------------------------------------------ EJERCICIO 3   solo_pares.py

numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio\n"))
i=0
while i<= numero_ingresado:
    if i%2==0:
        print("soy par: {}".format(i))
    i +=1        
