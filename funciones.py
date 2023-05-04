#Elaborado por Josue Salazar ,Jenny King 
#Fecha de creacion 29/04/23 1:20pm
#Ultima modificacion 29/04/23 1:20pm
#version 3.10.6
#importacion de librerias
import wikipedia
import time
import random
import re
from os import system
import xml.etree.ElementTree as ET
from archivos import *
from unidecode import unidecode
import pandas as pd
import datetime

wikipedia.set_lang("es")

"""
miZoo=Lista de animales
matriz= Matriz con los expedientes de los animales
"""

nombre='zoologico'
informacion='infoZoo'

def validarNumero(numero):
    '''
    Funcion:validar que el numero ingresado sea un entero positivo
    Entradas:
    - numeros(int)
    Salidas:
    -numero(int)
    '''
    if numero<=0:
        print("No se pueden ingresar valores menores a cero")
        numero=int(input('Digite el numero de animales aleatorios que quiere ingresar al zoo: '))
        validarNumero(numero)  
    return numero

def agregarAnimal():
    '''
    Funcion: Genera una lista de animales aleatorios para el zoologico
    Entradas:
    - path: direccion del archivo txt con los animales
    - numero(int): cantidad de animales aleatorios que va a agregar
    Salidas:
    - miZoo(list): lista con los animales del zoologico
    '''
    while True:
        try:
            print(f"Ingrese la direccion del archivo")
            print(r"Recuerde que la ruta del archivo debe ser similar a: C:\Users\quiro\OneDrive\Escritorio\Animales.txt")
            print("")
            path=(input("Ruta del archivo:"))
            open(path)
            numero=int(input('Digite el numero de animales aleatorios que quiere ingresar al zoo: '))
            numero=validarNumero(numero)
            system("cls")
            miZoo=[]
            i = 0
            while i < numero:
                linea = open(path,encoding="utf8").read().splitlines()
                animal= random.choice(linea)
                while animal not in miZoo:
                    miZoo.append(animal)
                    i+=1
                else:
                    animal= random.choice(linea)
            print(f"Animales seleccionados:")
            for animal in miZoo:
                print(animal)
            graba(nombre,miZoo)
            time.sleep(4.5)
            return miZoo
        except ValueError:
            system("cls")
            print("Debe ingresar unicamente un numero entero")
            print("Reanudando proceso")
            time.sleep(4.5)
            system("cls")
        except FileNotFoundError:
            system("cls")
            print("El archivo no ha sido localizado\n"+
                  "Revise la ruta ingresada")
            print("Reanudando proceso")
            time.sleep(4.5)
            system("cls")
        except IndexError:
            system("cls")
            print("No hay tantos animales en la lista.\n"+
                  "Revise que el numero ingresado sea menor al numero de animales en la lista")
            print("Reanudando proceso")
            time.sleep(4.5)
            system("cls")
        except PermissionError:
            system("cls")
            print("Error con los permisos del archivo ")
            print("Reanudando proceso")
            time.sleep(4.5)
            system("cls") 
        except OSError:
            system("cls")
            print("Error de sistema")
            print("Reanudando proceso")
            time.sleep(4.5)
            system("cls")
            
def limpiarTexto(resumen):
    '''
    Funcion: Limpia numeros de pie y otros caracteres del texto extraido
    Entradas:
    - resumen(str): resumen del animal sacado de wikipedia
    Salidas:
    - resumen(str): sin numeros de pie o caracteres especiales
    '''
    resumen = re.sub(r'\[.*?\]+', '', resumen)
    resumen = resumen.replace('\u200b', '')
    return resumen

def crearExpediente(miZoo):
    '''
    Funcion: Crea un expediente para cada animal y lo añade a una matriz
    Entradas:
    -miZoo(list)
    Salidas:
    - matriz(matrix): contiene los expedientes de todos los animales del zoologico
    '''
    matriz=[]
    expediente=[]
    while True:
        try:
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
            print(matriz)
            graba(informacion,matriz)
            time.sleep(7.5)
            return matriz
        except TypeError:
            print('No se a creado un Zoologico aun\nSe le redirigira a la opcion para crear un zoologico')
            time.sleep(5.5)
            system("cls")
            agregarAnimal()

def validarBusqueda(matriz):
    '''
    Funcion: Validar que el animal a buscar exista en el zoologico
    Entradas:
    - matriz(matrix)
    Salidas:
    - buscarAnimal(str): devuelve despues de normalizar el str, quitar tildes y caracteres especiales
    '''
    while True:
        if lee(nombre)== False:
            print('Se le rediccionara a la opcion para crear animales del zoologico.')
            time.sleep(5.5)
            system("cls")
            agregarAnimal()
        else:
            print('Los animales en el zoologico:',lee(nombre)) 
            buscarAnimal=input('Ingrese el nombre del animal a buscar: ')
            if buscarAnimal.isdigit()== True:
                print('Ingrese el nombre del animal, no se permiten valores numericos.\n')
            else:
                buscarAnimal=unidecode(buscarAnimal).lower()
                for fila in matriz:
                    for animal in fila:
                        if animal == buscarAnimal:
                            return buscarAnimal
                print('El animal a buscar no existe dentro del zoologico.\n')
            
def registrarAnotaciones(matriz): #anotaciones estan en la posicion 5 de cada lista en la matriz
    '''
    Funcion: Registrar anotaciones para cada animal en el zoologico
    Entradas:
    - matriz(matrix)
    Salidas:
    - matriz(matrix)
    '''
    respuesta=int(input("Quiere realizar una anotacion?:\nDigite [1] para Si \nDigite [2] para no \nRespuesta:"))
    print('')
    while respuesta == 1:
        buscarAnimal=validarBusqueda(matriz)
        for i in range(len(matriz)): #busca al animal en la matriz
            expediente= matriz[i]
            animal=expediente[0]
            if buscarAnimal == animal:
                anotacion=input('Anotacion: ')
                expediente[5].append(anotacion)
                graba(informacion,matriz)
                print('Anotacion guardada!\n')
        
        respuesta=int(input("Quiere realizar una anotacion?: Digite [1] para Si Digite [2] para no Respuesta:")) 
        system("cls")
    print(matriz)
    time.sleep(20)      
    return matriz

def validarApartado(miZoo):
    '''
    Funcion: valida que el numero de animales por apartar no sobrepase los animales existentes
    Entradas:
    - miZoo(lista)
    Salidas:
    - apartar(int): numero de animales por apartar validado
    '''
    while True:
        try:
            if lee(nombre)== False:
                print('Se le rediccionara a la opcion para crear animales del zoologico.')
                time.sleep(5.5)
                system("cls")
                agregarAnimal()
            else:   
                apartar=int(input('Digite el numero de animales que desea apartar del Zoologico: '))
                if apartar > len(miZoo):
                    print('El numero de animales por apartar es mayor al numero de animales en el Zoologico')
                return apartar
        except:
            print('Debe indicar un valor numerico de animales para apartar.\n')
            

def apartarAnimales(miZoo,matriz):
    '''
    Funcion: aparta animales del zoologico
    Entradas:
    - miZoo(list)
    - matriz(matrix)
    Salidas:
    - matriz(matrix)
    '''
    apartar=validarApartado(miZoo)
    i=0
    confirmacion=int(input(f'¿Está seguro que quiere apartar {apartar} animales de su Zoologico?\n'+
                           'Digite [1] para SI\nDigite [2] para NO\nRespuesta:'))
    if confirmacion == 1:
        while i < apartar:
            apartado= random.randint(1,len(matriz))
            #print(apartado,len(matriz))
            nombreAnimal=matriz[apartado-1][0]
            matriz.remove(matriz[apartado-1])
            graba(informacion,matriz)
            print('El animal:',nombreAnimal,'se ha apartado exitosamente.')
            print(matriz)
            i+=1
        time.sleep(20)
        return matriz
    print('Apartado abortado. No se aparto ningun animal. Volviendo al menu')
    time.sleep(3)
    system("cls")
    return''

def exportarDB(matriz): #crear XML
    '''
    Funcion: Crea una base de datos formato xml con los datos de la matriz
    Entradas:
    - matriz(matrix)
    Salidas:
    - tree(archivo xml)
    '''
    # crear etiqueta root
    root=ET.Element('root')
    #crear sub elemento
    root=ET.SubElement(root,'root')
    #insertar lista en subelemento
    for i in range(len(matriz)):
        expediente= ET.SubElement(root,'expediente')
        expediente.text =str(matriz[i])
    tree = ET.ElementTree(root)
    nombre= input('Determine un nombre para guardar el archivo:')+'.xml'
    graba(nombre,tree)
    print(nombre , 'Se creo y guardo con exito!')
    time.sleep(3)
    system("cls")
    return tree

def crearTablaHTML(matriz):
    nombre=[]
    nombreCientifico=[]
    linkReferencia=[]
    descripcion=[]
    linkImagen=[]
    anotaciones=[]
    indices=[]

    for indice,animal in enumerate(matriz):
        nombre.append(animal[0])
        nombreCientifico.append(animal[1])
        linkReferencia.append(animal[2])
        descripcion.append(animal[3])
        linkImagen.append(animal[4])
        anotaciones.append(animal[5])
        indices.append(indice+1)

    dicTabla={'Nombre': nombre, 'Nombre Cientifico': nombreCientifico, 'link Referencia':linkReferencia, 
            'descripcion': descripcion, 'link Imagenes':linkImagen, 'anotaciones':anotaciones }
    tabla=pd.DataFrame(data=dicTabla, index= indices)
    tabla=str(tabla.to_html(justify="center",render_links=True))
    fecha=datetime.datetime.now()
    formato=fecha.strftime('%d-%m-%Y-%H-%M-%S')+".html"
    grabaNoBinario(formato,tabla)
    



