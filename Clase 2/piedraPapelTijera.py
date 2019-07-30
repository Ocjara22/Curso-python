import random
import sys


juegadaJugador = sys.argv[1]

jugadaMaquina = random.choice['piedra','papel','tijera']

if juegadaJugador == jugadaMaquina:
    print("empate")
else:
    if juegadaJugador == 'piedra':
        if jugadaMaquina == 'papel':
            print ("pierdes")
        else:
            print("ganaste")
    elif juegadaJugador == 'piedra':
        if jugadaMaquina == 'papel':
            print ("pierdes")
        else:
            print("ganaste")
    else juegadaJugador == 'piedra':
        if jugadaMaquina == 'papel':
            print ("pierdes")
        else:
            print("ganaste")
    