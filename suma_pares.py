#------------------------------------------ EJERCICIO 6 suma_pares.py

numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio\n"))
i=1
suma = 0
while i<= numero_ingresado:
    if i%2==0:
        suma = suma + i
    i +=1        
print("El resultado de la suma de los pares es: {}".format(suma))

