#  calculo de velocidad de escape

# import sys
# import math;

# gravedad = float(sys.argv[1])
# radio = float(sys.argv[2]);

# print("El valor de la gravedad es : {}".format(gravedad))
# print("El valor del radio es en KM: {} ".format(radio))

# radioMetros = radio*1000

# valorConRaiz = (2*gravedad)*radioMetros

# print("Valor con raiz : {}".format(valorConRaiz))

# velocidadEscape = math.sqrt(valorConRaiz)

# print("resutado es : {}".format(velocidadEscape))




# precio venta * usuario - gastos

# si es positivo paga el 35% de impuesto




# emprendedor 1

# import sys

# precio = float(sys.argv[1])

# usuarios = float(sys.argv[2])

# gastos = float(sys.argv[3])

# utilidad = (precio * usuarios)- gastos

# if utilidad > 0:
#     rentabilidad = (utilidad*0,35)
#     print("Es rentable \n")
# else:
#     print ("No es rentable \n")




# emprendedor 2

# import sys 

# precio = float(sys.argv[1])
# usuariosTotales = float(sys.argv[2])
# usuariosPremium = float(sys.argv[3])
# usuariosGratuitos = float(sys.argv[4])
# gastos = float(sys.argv[5])

# utilidad = (precio * usuariosPremium) * 2 - gastos

# if utilidad > 0:
#     rentabilidad = (utilidad*0,35)
#     print("Es rentable \n")
# else:
#     print ("No es rentable \n")




# emprendedor 3

import sys 

precio = float(sys.argv[1])
usuariosTotales = float(sys.argv[2])
gastos = float(sys.argv[3])
utilidadAnterior = 0

if len(sys.argv) == 5:
    utilidadAnterior = float(sys.argv[4]) 
    print ("utilidad año anterior existe") 
elif len(sys.argv) == 4:
    utilidadAnterior= 1000
else:
    print("Programa no valido")

utilidad = (precio * usuariosTotales) - gastos

razon = utilidad/ utilidadAnterior

print("razon de utilidad de ahora es a anterior \n")
print (razon)
if utilidad > 0:
    rentabilidad = (utilidad*0.35)
    print("Es rentable \n")
    print (rentabilidad)
else:
    print ("No es rentable \n")

