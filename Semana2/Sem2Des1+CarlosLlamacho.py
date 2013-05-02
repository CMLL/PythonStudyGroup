#Grupo de estudio de Python G+.

#Unidad 2 - Desafio 1

"""Escribir un programa que convierta de numeros decimales a binarios."""

#Carlos Llamacho

def binario(decimal):
	
	resultado = ""
	
	while decimal != 0:
		resultado += str(decimal % 2)
		decimal = decimal / 2 	
	
	return resultado
	
in __name__=="__main__":
	decimal = int(input("Introduce un numero decimal: "))
	
	print(binario(decimal))
