


def letra_o(numero):
    string = ""
    for i in range(10):
        for j in range(10):
           if i<9 and i>0 and  j>0 and j<9:
               string += " " 
           else:
               string +="*"
               
        string += "\n"
    print(string)

def letra_i(numero):
    string = ""
    for i in range(9):
        for j in range(9):
            if (i == 0  or  i== 8) or (j == int(9/2)):
                string += "*"
            else:
                string += " "
        string += "\n"
    print(string) 

def letra_x(numero):
    string = ""
    for i in range(10):
        for j in range(10):
            if (i == j) or (j+i == 10-1):
                string += "*"
            else:
                string += " "
        string += "\n"
    print(string) 

letra_x(10)