import sys
from string import ascii_lowercase



def gen(numeroFuncion):
    char = ascii_lowercase
    patron = ""
    print(char)

    for i in range(0, numeroFuncion):
        patron += char[i]
        print(char[i])

    print ("el resultado final es \n")
    print (patron)
    return 0





numero = int(sys.argv[1])
gen(numero)



