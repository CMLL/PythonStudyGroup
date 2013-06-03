# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:33:05 2013

@author: cllamach

Desafio 2 - Grupo de Estudio Python - Unidades 8 y 9.

Crear un diccionario con los participantes de un curso, ingresando:

Nombre.
Apellido.
Edad.
Teléfono.
Correo Electrónico.
Localidad.

El programa nos debe permitir gerenciar esa lista agregando o eliminando 
participantes y también corrigiendo datos. Generar informes permitiendo al
usuario elegir qué columnas (Nombre, Apellido, etc.) quiere imprimir en pantalla.
"""

def menu():
	
	print("Menu: ")
	print("-"*25)
	print("1-Agregar datos.")
	print("2-Ver datos.")
	print("3-Eliminar datos.")
	print("4-Editar datos.")
	print("5-Informes.")
	print("6-Salir.")
	print("-"*25)
	opcion = int(input("Seleccione la opcion deseada(1-6): "))
	
	while opcion not in range(1,7):
		opcion = int(input("Su seleccion no es una opcion valida, intente nuevamente(1-6): "))
		

def main():
	menu()
	
if __name__=="__main__":
	main()
