#Grupo de estudio de Python
#Semana 1 - Desafio 3

#Ingresar cuatro valores y que dibuje 4 barras del tamaño de los valores ingresados.

#Realizado por Carlos Llamacho

# -*- coding: utf8 -*-

barras = []

def desafio3():

    maximo = int(input("Tamaño maximo: "))

    for item in range(4):
        barras.append(int(input("Introduzca el tamaño de la barra " + str(item + 1) + ": ")))

    print("*" * 22)

    for i in range(maximo):
    	
    print("*" * 22)


if __name__=="__main__":
    desafio3()

