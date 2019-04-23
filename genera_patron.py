#------------------------------------------ EJERCICIO 7 genera_patron.py

numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio\n"))
i=1
patron = ""
while i<= numero_ingresado:
    patron=patron+str(i)
    print(patron)
    i += 1
