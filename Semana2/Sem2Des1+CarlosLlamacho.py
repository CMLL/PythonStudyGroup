#Grupo de estudio de Python G+.

#Unidad 2 - Desafio 1

"""Escribir un programa que convierta de numeros decimales a binarios."""

#Carlos Llamacho

def binario(decimal):
	
	resultado = ""
	
	#Loop para el algoritmo.
	while decimal != 0:
		#Resto del numero a convertir, este es el numero binario.
		resultado += str(decimal % 2)
		#Esto reduce el numero decimal hasta que se convierte en 0.
		decimal = decimal // 2
		
	return resultado

if __name__=="__main__":
	decimal = int(input("Introduce un numero decimal: "))
	
	print(binario(decimal))
