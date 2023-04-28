import wikipedia
#import datetime
import random
import re
from os import system
from archivos import *
import xml.etree.ElementTree as ET

wikipedia.set_lang("es")
#ocupa un input del usuario con la direccion del 'texto.txt', debe mandarse eso como parametro

def agregarAnimal(texto,numero):
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
  print(miZoo)
  return crearExpediente(miZoo)

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
        anotaciones=['Anotaciones: ']
        expediente.extend([animal,titulo,url,resumen,imagen,anotaciones])
        matriz.append(expediente)
    print(matriz)
    return registrarAnotaciones(matriz)

def registrarAnotaciones (matriz): #anotaciones estan en la posicion 5 de cada lista en la matriz
    respuesta=int(input("Quiere realizar una anotacion?: Digite [1] para Si Digite [2] para no Respuesta:"))
    while respuesta == 1:
        buscarAnimal=input('Indique el nombre del animal al cual quiere añadir una anotación: ')#validar nombre de animal en minusculas y sin caracteres especiales
        for i in range(len(matriz)): #busca al animal en la matriz
            expediente= matriz[i]
            animal=expediente[0]
            if buscarAnimal == animal:
                anotacion=input('Anotacion')
                expediente[5].append(anotacion)
        respuesta=int(input("Quiere realizar una anotacion?: Digite [1] para Si Digite [2] para no Respuesta:"))  
    print(matriz)     
    return apartarAnimales(matriz)

def apartarAnimales(matriz):
    apartar=int(input('Cuantos animales quiere apartar?: '))#hay que validar que no sea mayor al numero de animales en el zoologico
    i=0
    while i< apartar:
        apartado= random.randint(1,len(matriz))
        print(apartado,len(matriz))
        #animal=matriz[apartado]
        print('El animal:',matriz[apartado-1][0],'se ha apartado exitosamente.')
        matriz.remove(matriz[apartado-1])
        print(matriz)
        i+=1
    return matriz
 
matriz=[['perro', 'Canis familiaris', 'https://es.wikipedia.org/wiki/Canis_familiaris', 'El perro (Canis familiaris o Canis lupus familiaris, dependiendo de si se lo considera una especie por derecho propio o una subespecie del lobo), llamado perro doméstico o can, y en algunos lugares coloquialmente llamado chucho, tuso, choco, entre otros; es un mamífero carnívoro de la familia de los cánidos, que constituye una especie del género Canis. En el 2013, la población mundial estimada de perros estaba entre setecientos millones y novecientos ochenta y siete millones. Su tamaño (o talla), su forma y su pelaje es muy diverso y varía según la raza. Posee un oído y un olfato muy desarrollados, y este último es su principal órgano sensorial.', 'https://upload.wikimedia.org/wikipedia/commons/3/38/Anatomy_dog.png', []],
        ['gato', 'Felis silvestris catus', 'https://es.wikipedia.org/wiki/Felis_silvestris_catus', 'El gato doméstico (Felis silvestris catus), llamado más comúnmente gato, y de forma coloquial minino, michino, michi, micho, mizo, miz, morroño o morrongo, y algunos nombres más, es un mamífero carnívoro de la familia Felidae. Es una subespecie domesticada, por la convivencia con el ser humano, del gato montés.', 'https://upload.wikimedia.org/wikipedia/commons/f/f3/Cachorro_de_gato.jpg', []],
        ['zorro', 'Vulpini', 'https://es.wikipedia.org/wiki/Vulpini', 'Los vulpinos (Vulpini) son una tribu de mamíferos carnívoros incluidos en la familia de los cánidos. Se conocen comúnmente como zorros o raposas.\nActualmente están representados por unas 27 especies que se encuentran en casi todos los continentes, aunque la más extendida es el zorro rojo o zorro común (Vulpes vulpes), que habita en Europa y América del Norte.', 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Commons-logo.svg', []],
        ['leon', 'Panthera leo', 'https://es.wikipedia.org/wiki/Panthera_leo', 'El león (Panthera leo) es un mamífero carnívoro de la familia de los félidos y una de las cinco especies del género Panthera. Los leones salvajes viven en poblaciones cada vez más dispersas y fragmentadas del África subsahariana (a excepción de las regiones selváticas de la costa del Atlántico y la cuenca del Congo) y una pequeña zona del noroeste de India (una población en peligro crítico en el parque nacional del Bosque de Gir y alrededores), habiendo desaparecido del resto de Asia del Sur, Asia Occidental, África del Norte y la península balcánica en tiempos históricos.', 'https://upload.wikimedia.org/wikipedia/commons/a/ae/African_Lion_Panthera_leo_Male_Pittsburgh_2800px.jpg', []]] 
def crearXML(matriz):
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
    print(nombre)
    graba(nombre,tree)


texto= (r'C:\Users\jenki\OneDrive\Escritorio\texto.txt') 
numero = int(input('Digite un numero: '))
agregarAnimal(texto,numero)

agregarAnimal(texto,numero)