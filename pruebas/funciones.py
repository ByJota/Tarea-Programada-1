# demo de Funciones, sin validadciones
#importacion de librerias
import wikipedia
#import datetime
import random
import re
from os import system
import xml.etree.ElementTree as ET
wikipedia.set_lang("es")
#def funciones

def agregarAnimal(texto):
  numero = int(input('Digite un numero: '))
  miZoo=[]
  i = 0
  while i < numero:
    linea = open(texto,encoding="utf8").read().splitlines()
    animal= random.choice(linea)
    while animal not in miZoo:
      miZoo.append(animal)
      i+=1
    else:
      animal= random.choice(linea)
  print(miZoo,'\nSe creo lista de animales exitosamente.')
  return miZoo 

def limpiarTexto(resumen):
    resumen = re.sub(r'\[.*?\]+', '', resumen)
    resumen = resumen.replace('\u200b', '')
    return resumen

def crearExpediente(miZoo):
    matriz=[]
    expediente=[]
    for i in range(len(miZoo)):
        expediente=[]
        animal=miZoo[i]
        titulo= wikipedia.page(animal).title
        url= wikipedia.page(animal).url
        resumen= limpiarTexto(wikipedia.summary(animal,sentences=2))
        imagen= wikipedia.page(animal).images[1]
        anotaciones=[]
        expediente.extend([animal,titulo,url,resumen,imagen,anotaciones])
        matriz.append(expediente)
    return matriz

def registrarAnotaciones (matriz): #anotaciones estan en la posicion 5 de cada lista en la matriz
    respuesta=int(input("Quiere realizar una anotacion?: Digite [1] para Si Digite [2] para no Respuesta:"))
    while respuesta == 1:
        buscarAnimal=input('Indique el nombre del animal al cual quiere añadir una anotación: ')#validar nombre de animal en minusculas y sin caracteres especiales
        for i in range(len(matriz)): #busca al animal en la matriz
            expediente= matriz[i]
            animal=expediente[0]
            if buscarAnimal == animal:
                anotacion=input('Anotacion: ')
                expediente[5].append(anotacion)
        respuesta=int(input("Quiere realizar una anotacion?: Digite [1] para Si Digite [2] para no Respuesta:"))         
    return matriz

def apartarAnimales(matriz):
    apartar=int(input('Cuantos animales quiere apartar?: '))# hay que validar que no sea mayor al numero de animales en el zoologico
    i=0
    while i< apartar:
        apartado= random.randint(1,len(matriz))
        print(apartado,len(matriz))
        print('El animal:',matriz[apartado-1][0],'se ha apartado exitosamente.')
        matriz.remove(matriz[apartado-1])
        print(matriz)
        i+=1
    return matriz


# fecha= datetime.datetime.now()
# formato= fecha.strftime('%d-%m-%Y-%H-%M-%S')
# print(formato)

#programa principal
#numero = int(input('Digite un numero: '))
texto = (r'C:\Users\jenki\OneDrive - Estudiantes ITCR\TP#1\pruebas\texto.txt')

def menu():
    print("Sistema de Información del Zoológico".center(70,'='))
    print("Menu de opciones:\n"+
        "1)Agregar animales\n"+
        "2)Crear expediente\n"+
        "3)Registrar Anotaciones\n"+
        "4)Apartar animales de mi zoológico\n"+
        "5)Exportando la base de datos\n"+
        "6)Mostrar base de datos del zoológico\n"+
        "7)Salir del sistema de información\n") 
    
    opcion=int(input("Opcion:"))
    if opcion==1:
        system("cls")
        agregarAnimal(texto)
    elif opcion==2:
        system("cls")
        crearExpediente()
    elif opcion==3:
        system("cls")
        registrarAnotaciones()
    elif opcion==4:
        system("cls")
        apartarAnimales()
    elif opcion==5:
        system("cls")
        #exportarDB()
    elif opcion==6:
        system("cls")
        #mostrarDB()
    elif opcion==7:
        print("¿Seguro que quiere salir del Programa?\n"+
              "1.Si\n"+
              "2.No")
        respuesta=int(input("R/"))
        if respuesta==1:
            system("exit")
        else:
            system("cls")
            menu()
    else:
        print("Opcion invalida. Debe seleccionar una opción del 1 al 7. ")
    return