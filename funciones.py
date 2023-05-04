#Elaborado por Josue Salazar ,Jenny King 
#Fecha de creacion 29/04/23 1:20pm
#Ultima modificacion 29/04/23 1:20pm
#version 3.10.6
#importacion de librerias
import wikipedia
import time
import random
import re
import os
import xml.etree.ElementTree as ET
from archivos import *
from unidecode import unidecode
import codecs as cd
import datetime
import webbrowser

wikipedia.set_lang("es")

"""
miZoo=Lista de animales
matriz= Matriz con los expedientes de los animales
"""

def recuperarLista(matriz):
    '''
    Funcion: Recupera una lista simple con los nombres de los animales de la matriz
    Entradas:
    -matriz(matrix)
    Salidas:
    - lista(list)
    '''
    lista=[]
    for i in range(len(matriz)):
        animal= matriz[i][0]
        lista.append(animal)
    return lista

r=int(input('¿Desea cargar un zoológico anterior?\nDigite [1] para Si\nDigite [2] para no\nRespuesta:'))
if r==1:
    archivo=input('Ingrese la dirección del archivo anterior: ')
    matriz=leeInfo(archivo)
    nombre=input('Ingrese un nombre para guardar los animales de este zoológico:')
    miZoo=recuperarLista(matriz)
    informacion=nombre+'info'
    graba(informacion,matriz)
    graba(nombre,miZoo)
    pass
else:
    os.system("cls")
    x=0
    while x < 1:
        nombreZoo=input('Ingrese un nombre para su zoológico:')
        print('')
        x=1
        nombre=nombreZoo
        informacion=nombreZoo+'info'
        
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
    Funcion: Genera una lista de animales aleatorios para el zoológico
    Entradas:
    - path: direccion del archivo txt con los animales
    - numero(int): cantidad de animales aleatorios que va a agregar
    Salidas:
    - miZoo(list): lista con los animales del zoológico
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
            os.system("cls")
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
            input("Presione Enter para continuar:")
            return miZoo
        except ValueError:
            os.system("cls")
            print("Debe ingresar unicamente un numero entero")
            print("Reanudando proceso")
            time.sleep(4.5)
            os.system("cls")
        except FileNotFoundError:
            os.system("cls")
            print("El archivo no ha sido localizado\n"+
                  "Revise la ruta ingresada")
            print("Reanudando proceso")
            time.sleep(4.5)
            os.system("cls")
        except IndexError:
            os.system("cls")
            print("No hay tantos animales en la lista.\n"+
                  "Revise que el numero ingresado sea menor al numero de animales en la lista")
            print("Reanudando proceso")
            time.sleep(4.5)
            os.system("cls")
        except PermissionError:
            os.system("cls")
            print("Error con los permisos del archivo ")
            print("Reanudando proceso")
            time.sleep(4.5)
            os.system("cls") 
        except OSError:
            os.system("cls")
            print("Error de sistema")
            print("Reanudando proceso")
            time.sleep(4.5)
            os.system("cls")
            
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
    - matriz(matrix): contiene los expedientes de todos los animales del zoológico
    '''
    matriz=[]
    expediente=[]
    print('Esto puede tardar un poco, porfavor espere...')
    if len(miZoo)>=8:
        print("Advertencia: Este proceso puede tardar un poco mas debido a que ha seleccionado muchos animales.\n"+
              "Por favor sea paciente ")
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
            os.system("cls")
            for fila in matriz:
                print(fila)
                print("")
            input("Presione Enter para continuar:")
            return matriz
        except TypeError:
            print('No se a creado un zoológico aun\nSe le redirigira a la opción para crear un zoológico')
            input("Presione Enter para continuar:")
            os.system("cls")
            agregarAnimal()

def validarBusqueda(matriz):
    '''
    Funcion: Validar que el animal a buscar exista en el zoológico
    Entradas:
    - matriz(matrix)
    Salidas:
    - buscarAnimal(str): devuelve despues de normalizar el str, quitar tildes y caracteres especiales
    '''
    while True:
        if lee(nombre)== False:
            print('Se le rediccionara a la opción para crear animales del zoológico.')
            input("Presione Enter para continuar:")
            os.system("cls")
            agregarAnimal()
        else:
            print('Los animales en el zoológico:',lee(nombre)) 
            buscarAnimal=input('Ingrese el nombre del animal a buscar: ')
            print('')
            if buscarAnimal.isdigit()== True:
                print('Ingrese el nombre del animal, no se permiten valores numéricos.\n')
            else:
                buscarAnimal=unidecode(buscarAnimal)#.lower()
                for fila in matriz:
                    for animal in fila:
                        if animal == buscarAnimal:
                            return buscarAnimal
                print('El animal a buscar no existe dentro del zoológico.\n')
            
def registrarAnotaciones(matriz): #anotaciones estan en la posicion 5 de cada lista en la matriz
    '''
    Funcion: Registrar anotaciones para cada animal en el zoológico
    Entradas:
    - matriz(matrix)
    Salidas:
    - matriz(matrix)
    '''
    print("Registrar Anotaciones".center(70,"=")+"\n")
    respuesta=int(input("Quiere realizar una anotacion?:\nDigite [1] para Si \nDigite [2] para no \nRespuesta:"))
    print('Nota al usuario: Para que evitar cualquie tipo de dificultad, copie el nombre del animal al cual le vaya a realizar una anotacion.'
          '\nEl sistema es sensible a las mayúsculas.')
    while respuesta == 1:
        buscarAnimal=validarBusqueda(matriz)
        for i in range(len(matriz)): #busca al animal en la matriz
            expediente= matriz[i]
            animal=expediente[0]
            if buscarAnimal == animal:
                anotacion=input('Anotación: ')
                expediente[5].append(anotacion)
                graba(informacion,matriz)
                print('¡Anotación guardada!\n')
        
        respuesta=int(input("Quiere realizar una anotación?:\nDigite [1] para Si\nDigite [2] para no\nRespuesta:")) 
        os.system("cls")
    for fila in matriz:
        print(fila)
    input("Presione Enter para continuar:")     
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
                print('Se le rediccionara a la opción para crear animales del zoológico.')
                input("Presione Enter para continuar:") 
                os.system("cls")
                agregarAnimal()
            else:   
                apartar=int(input('Digite el numero de animales que desea apartar del zoológico: '))
                if apartar > len(miZoo):
                    print('El numero de animales por apartar es mayor al numero de animales en el zoológico')
                return apartar
        except:
            print('Debe indicar un valor numérico de animales para apartar.\n')
            
def apartarAnimales(miZoo,matriz):
    '''
    Funcion: aparta animales del zoológico
    Entradas:
    - miZoo(list)
    - matriz(matrix)
    Salidas:
    - matriz(matrix)
    '''
    print("Apartar Animales".center(70,"=")+"\n")
    apartar=validarApartado(miZoo)
    i=0
    confirmacion=int(input(f'¿Está seguro que quiere apartar {apartar} animales de su zoológico?\n'+
                           'Digite [1] para SI\nDigite [2] para NO\nRespuesta:'))
    if confirmacion == 1:
        while i < apartar:
            apartado= random.randint(1,len(matriz))
            nombreAnimal=matriz[apartado-1][0]
            matriz.remove(matriz[apartado-1])
            graba(informacion,matriz)
            print('')
            print('El animal:',nombreAnimal,'se ha apartado exitosamente.')
            print(matriz)
            i+=1
        for fila in matriz:
            print(fila)
        input("\nPresione Enter para continuar:")
        return matriz
    print('Apartado abortado. No se aparto ningun animal. Volviendo al menu')
    input("\nPresione Enter para continuar:")
    os.system("cls")
    return''

def exportarDB(matriz): #crear XML
    '''
    Funcion: Crea una base de datos formato xml con los datos de la matriz
    Entradas:
    - matriz(matrix)
    Salidas:
    - tree(archivo xml)
    '''
    root=ET.Element('root')# crear etiqueta root, header
    root=ET.SubElement(root,'root')#crear sub elemento del root
    for i in range(len(matriz)):#insertar lista en sub elemento
        expediente= ET.SubElement(root,'expediente')
        expediente.text =str(matriz[i])
    tree = ET.ElementTree(root)
    nombre= input('Determine un nombre para guardar el archivo:')+'.xml'
    graba(nombre,tree)
    print(nombre , 'Se creo y guardo con exito!')
    input("\nPresione Enter para continuar:")
    os.system("cls")
    return tree

def crearTablaHTML(matriz):
    '''
    Funcion: Crea una tabla html en el navegador usando los datos de la matriz
    Entradas:
    - matriz(matrix)
    Salidas:
    - tabla html
    '''
    print("Trabajando en la tabla, por favor espere un momento")
    fecha=datetime.datetime.now()
    formato="BD-"+fecha.strftime('%d-%m-%Y-%H-%M-%S')+".html"
    with cd.open(formato,'w','utf-8') as f:
        f.write('<table style="background-color: #E1E1E1>\n')
        f.write('<thead style="background-color: #B2FF01>\n')
        f.write('<tr>\n')
        f.write('<th>Nombre</th>\n')
        f.write('<th>Título</th>\n')
        f.write('<th>Url</th>\n')
        f.write('<th>Resumen</th>\n')
        f.write('<th>Imagenes</th>\n')
        f.write('<th>Anotaciones</th>\n') 
        f.write('</tr>\n')
        f.write('</thead>\n')
        f.write('<tbody>\n')
        for linea in matriz:
            f.write('<tr>\n')
            for columna in linea:
                f.write('<td>{}</td>\n'.format(columna))
            f.write('</tr>\n')
        f.write('</tbody>\n')
        f.write('</table>\n') 
    time.sleep(3)
    path=os.path.abspath(formato)
    webbrowser.open("file:///"+path)
    return "Tabla creada con exito"