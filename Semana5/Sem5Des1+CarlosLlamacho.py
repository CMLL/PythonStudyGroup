# -*- coding: utf-8 -*-
"""
Created on Wed May 29 19:14:01 2013

@author: Carlos Llamacho

Desafio Grupal Grupo de Estudio Python G+
"""

def main():
	"""Recoge los patrones de diseño y la cantidad de capas."""
	
	capas = int(input("Cuantas capas tendra el diseño: "))
	ancho = int(input("Cual es el ancho del patron: "))
	
	adquirir_disenos(capas, ancho)
	
def adquirir_disenos(cant_capas, ancho_diseno):

	disenos = []	
	
	for i in range(cant_capas):
		disenos.append(str(input("El diseño de la capa {0}: ".format(i))))
		separador = range(1, ancho_diseno)
		print(separador)
		print("|" + " \t" + "|")
	
	return disenos	
	
if __name__=="__main__":
	main()

