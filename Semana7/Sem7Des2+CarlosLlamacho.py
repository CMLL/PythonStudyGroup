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

from collections import OrderedDict
import sys

def menu(agenda):
	
	#Menu con las opciones. 1-6
	print("-"*25)
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
	
	#Funciones core de la agenda. Cada eleccion indicara el flujo.
	#Exceptuando la funcion 6 que sale del programa, todas regresan al menu.	
	if opcion == 1:
		agregar(agenda)
		menu(agenda)
	elif opcion == 2:
		ver(agenda)
		menu(agenda)
	elif opcion == 3:
		eliminar(agenda)
		menu(agenda)
	elif opcion == 6:
		sys.exit()

def agregar(agenda):
	
	siguiente = True
	
	#Loop que recoge datos hasta que se indique lo contrario.
	while siguiente:
		print("Datos a agregar al diccionario: ")
		print("-"*25)
		nombre = str(input("Nombre: "))
		apellido = str(input("Apellido : "))
		edad = int(input("Edad: "))
		telefono = int(input("Telefono: "))
		email = str(input("Email: "))
		localidad = str(input("Localidad: "))
		print("-"*25)
		
		agenda.append(OrderedDict([("nombre", nombre), ("apellido",apellido),("edad",edad), ("telefono",telefono), ("email",email),("localidad",localidad)]))			
		
		seguir = str(input("Quiere ingregsar otra persona a la agenda(Y/N): "))
		if seguir == "N" or seguir == "N".lower:
			siguiente = False
			
	return agenda
	
def ver(agenda):
	#Muestra todos los datos almacenados en la agenda.	
	for entrada in agenda:
		print("#"*50)
		for key in entrada:
			print(str(key) + ": " + str(entrada.get(key)))
	

def eliminar(agenda):
	
	print("Entradas en la agenda: ")
	contador = 0
	for entrada in agenda:
		print(str(contador) + " - "+ str(entrada.get("nombre")) +" "+ str(entrada.get("apellido")))
		contador +=1
	print("*"*25)
	eliminar = int(input("Seleccione la que quiera eliminar: "))
	while eliminar not in range(0, len(agenda)+1):
		eliminar = int(input("Seguro que eligio bien? Intente nuevamente: "))
	agenda.pop(eliminar)
	print("El dato fue eliminado.")	
			
		
def main():
	
	#Inicializar la agenda.
	agenda = []
	
	#Cargar el menu usando la agenda creada.
	menu(agenda)
	
if __name__=="__main__":
	main()
