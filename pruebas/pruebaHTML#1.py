import pandas as pd
import datetime
tabla=[['serpiente', 'Serpentes', 'https://es.wikipedia.org/wiki/Serpentes', 'Las serpientes (Serpentes) u ofidios (Ophidia) son un suborden de saurópsidos (reptiles) diápsidos pertenecientes al orden Squamata, del superorden Lepidosauria, caracterizado por la ausencia de patas (la pitón mantiene diminutas extremidades vestigiales, herencia de su pasado evolutivo) y el cuerpo muy alargado. Se originaron en el período Cretácico.', 'https://upload.wikimedia.org/wikipedia/commons/9/90/Bothriechis_schlegelii_%28La_Selva_Biological_Station%29.jpg', ['el pibe esta bien ','se encuentra chido']],
    ['perro ', 'Canis familiaris', 'https://es.wikipedia.org/wiki/Canis_familiaris', 'El perro (Canis familiaris o Canis lupus familiaris, dependiendo de si se lo considera una especie por derecho propio o una subespecie del lobo), llamado perro doméstico o can, y en algunos lugares coloquialmente llamado chucho, tuso, choco, entre otros; es un mamífero carnívoro de la familia de los cánidos, que constituye una especie del género Canis. En el 2013, la población mundial estimada de perros estaba entre setecientos millones y novecientos ochenta y siete millones. Su tamaño (o talla), su forma y su pelaje es muy diverso y varía según la raza. Posee un oído y un olfato muy desarrollados, y este último es su principal órgano sensorial.', 'https://upload.wikimedia.org/wikipedia/commons/3/38/Anatomy_dog.png', ['linda mi gorda']], 
    ['mono ', 'Mono', 'https://es.wikipedia.org/wiki/Mono', 'La palabra mono es un término informal, no taxonómico, que designa a un amplio conjunto de primates simiiformes. \nLos términos mono y simio son sinónimos en el idioma español, pero en zoología suele hacerse una distinción entre ambos, debido a la influencia del idioma inglés, en el que los términos equivalentes monkey y ape tienen diferentes significados.', 'https://upload.wikimedia.org/wikipedia/commons/8/84/Ateles_fusciceps_Colombia.JPG', ['monkey']], 
    ['gato', 'Felis silvestris catus', 'https://es.wikipedia.org/wiki/Felis_silvestris_catus', 'El gato doméstico (Felis silvestris catus), llamado más comúnmente gato, y de forma coloquial minino, michino, michi, micho, mizo, miz, morroño o morrongo, y algunos nombres más, es un mamífero carnívoro de la familia Felidae. Es una subespecie domesticada, por la convivencia con el ser humano, del gato montés.', 'https://upload.wikimedia.org/wikipedia/commons/f/f3/Cachorro_de_gato.jpg', ['El gato tuvo gatitos','la gata murio']], 
    ['ardilla', 'Ardilla', 'https://es.wikipedia.org/wiki/Ardilla', 'Se llama ardilla (del paleohispánico: harda ‘sin h y en diminutivo’) a ciertas especies de roedores esciuromorfos de la familia Sciuridae, entre las que se encuentran:\n\nLas especies del género Ratufa, el único de la subfamilia Ratufinae.\nLa ardilla pigmea neotropical (Sciurillus pusillus), la única especie de la subfamilia Sciurillinae.', 'https://upload.wikimedia.org/wikipedia/commons/c/cc/Ardilla_en_la_Plaza_Bol%C3%ADvar%2C_Caracas-Venezuela_II.JPG', ['una ardilla con una sandia','las ardillas nos dominaran a todos']], 
    ['ballena', 'Balaenidae', 'https://es.wikipedia.org/wiki/Balaenidae', 'Los balénidos (Balaenidae) son una familia de cetáceos misticetos que incluye cuatro especies, distribuidas en dos géneros, Balaena y Eubalaena. Sin embargo el término ballena es usado en sentido amplio para referirse a todos los grandes cetáceos incluidos en el parvorden Mysticeti (cetáceos con barbas) como el rorcual azul (Balaenoptera musculus) y a varias especies del parvorden Odontoceti (cetáceos dentados), por ejemplo el cachalote (Physeter macrocephalus).', 'https://upload.wikimedia.org/wikipedia/commons/b/b7/Bowhead.jpg', ['El monstruo del lago Ness=Pinga de ballena']]]
nombre=[]
nombreCientifico=[]
linkReferencia=[]
descripcion=[]
linkImagen=[]
anotaciones=[]
indices=[]

for indice,animal in enumerate(tabla):
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
formato=fecha.strftime('%d-%m-%Y-%H-%M-%S')





        
 