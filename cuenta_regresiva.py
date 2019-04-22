
# ---------------------------------------------EJERCICIO 1 cuenta_regresiva.py
i = 0
while i < 50:
    print("Iteración {}".format(i + 1))
    i +=1



cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
for i in range(cuenta_regresiva):
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))


cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
i=cuenta_regresiva
while i > 0:
    print("Iteración {}".format(i))
    i -=1



#------------------------------------------ EJERCICIO 2   solo_pares.py

numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio\n"))
i=0
while i<= numero_ingresado:
    if i%2==0:
        print("soy par: {}".format(i))
    i +=1        


#-------------------------------------------EJERCICIO 3 solo_pares_refactor.py

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

#------------------------------------------ EJERCICIO 4 solo_impares.py


numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio"))
i=1
while i<= numero_ingresado:
    if i%2!=0:
        print("soy impar: {}".format(i))
    i +=1   

#------------------------------------------ EJERCICIO 5 suma_pares.py

numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio\n"))
i=1
suma = 0
while i<= numero_ingresado:
    if i%2==0:
        suma = suma + i
    i +=1        
print("El resultado de la suma de los pares es: {}".format(suma))

#------------------------------------------ EJERCICIO 6 genera_patron.py

numero_ingresado = int(input("Ingrese numero para ejecutar ejercicio\n"))
i=1
patron = ""
while i<= numero_ingresado:
    patron=patron+str(i)
    print(patron)
    i += 1


#------------------------------------------ EJERCICIO 7 lorem_generator.py

import sys

print(sys.argv[0])
print(sys.argv[1])
paramotroUrl = int(sys.argv[1])
i=1

loremNisum= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus auctor ligula et tellus imperdiet, nec luctus risus pulvinar. Vestibulum odio sem, imperdiet et neque ac, tempus rhoncus odio. Etiam sollicitudin urna mi, at vestibulum nulla accumsan et. In ultricies sagittis lobortis. Quisque eleifend, felis id imperdiet bibendum, felis quam vulputate eros, non suscipit tellus orci vitae ex. Maecenas semper varius lobortis. Curabitur eu lorem ut dui molestie fermentum sed et nulla."

while i <= paramotroUrl:
    print("{} \n".format(loremNisum))
    i +=1

#------------------------------------------ EJERCICIO 8 fuerza_bruta.py


claveIngresada = input("Ingrese clave para ejecutar el ejercicio\n")
contador = 0
for i in claveIngresada:
    if i=="a" or i=="A":
        contador += 1
    if i=="b" or i=="B":
        contador += 1
    if i=="c" or i=="C":
        contador += 1
    if i=="d" or i=="D":
        contador += 1
    if i=="e" or i=="E":
        contador += 1
    if i=="f" or i=="F":
        contador += 1
    if i=="g" or i=="G":
        contador += 1
    if i=="h" or i=="H":
        contador += 1
    if i=="i" or i=="I":
        contador += 1
    if i=="j" or i=="J":
        contador += 1
    if i=="k" or i=="K":
        contador += 1
    if i=="l" or i=="L":
        contador += 1
    if i=="m" or i=="M":
        contador += 1
    if i=="n" or i=="N":
        contador += 1
    if i=="ñ" or i=="Ñ":
        contador += 1
    if i=="o" or i=="O":
        contador += 1
    if i=="p" or i=="P":
        contador += 1
    if i=="q" or i=="Q":
        conrador += 1
    if i=="r" or i=="R":
        contador += 1
    if i=="s" or i=="S":
        contador += 1
    if i=="t" or i=="T":
        contador += 1
    if i=="u" or i=="U":
        contador += 1
    if i=="v" or i=="V":
        contador += 1
    if i=="w" or i=="W":
        contador += 1
    if i=="x" or i=="X":
        contador += 1
    if i=="y" or i=="Y":
        contador += 1
    if i=="z" or i=="Z":
        contador += 1
print("No hay más letras. Se adivinó la palabra en {} intentos".format(contador))   
for indice in range(len(claveIngresada)):
    caracter = claveIngresada[indice]
    print("En el índice {} tenemos a '{}'".format(indice, caracter)