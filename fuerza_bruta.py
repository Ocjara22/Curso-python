#------------------------------------------ EJERCICIO 9 fuerza_bruta.py
claveIngresada = input("Ingrese clave para ejecutar el ejercicio\n")
contador = 0
caracteres ="abcdefghijklmnñopqrstuvwxyz"
for i in claveIngresada:
    for j in caracteres:
        print("estoy comparando {} con ".format(i), j)
        if i.lower()==j:
            contador +=1
            print(contador)
            print ("letra encontrada")
            break
        contador +=1
print (contador)