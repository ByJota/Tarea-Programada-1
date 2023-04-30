import wikipedia
import time
import random
import re
from os import system
import xml.etree.ElementTree as ET
wikipedia.set_lang("es")

def validarNumero(numero):
    if numero<=0:
        print("No se pueden ingresar valores menores a cero")
        numero=int(input('Digite el numero de animales aleatorios que quiere ingresar al zoo: '))
        validarNumero(numero)
    
    return numero

def agregarAnimal():
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
            time.sleep(4.5)
            return crearExpediente(miZoo)
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
            '''
        except OSError:
            system("cls")
            print("Error de sistema")
            print("Reanudando proceso")
            time.sleep(4.5)
            system("cls")
            '''

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


