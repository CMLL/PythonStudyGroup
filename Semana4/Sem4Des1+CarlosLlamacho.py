# -*- coding= utf-8 -*-

#Grupo de estudio Python

#Semana 4 - Desafio 1

#Una funcion que reciba un array (de lo que sea) y devuelva un array sin repeticiones.

#Autor:
#Carlos Llamacho

def sin_repetir(datos):

  for item in datos:
    if datos.count(item) > 1:
      datos.pop(item)

  return datos

if __name__="__main__":

  print(sin_repetir([]))
  print(sin_repetir([1,3,1,3]))
  print(sin_repetir([1,3,5,6,6,5,3,1,9711])