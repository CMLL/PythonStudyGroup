#Grupo de estudio de Python.
#Desafio 4

#Realizado por Carlos Llamacho

# -*- coding: utf8 -*-

def desafio4():
	
	numero = int(input("Dame un numero: "))
	
	lista = [range(1, numero+1)]
	
	for i in range(numero):
		print(" " * (numero- i) + str(i+1) + " " * (numero - i))



if __name__=="__main__":
	desafio4()
