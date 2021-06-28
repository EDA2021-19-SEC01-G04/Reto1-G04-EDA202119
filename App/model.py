"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sb
from DISClib.Algorithms.Sorting import insertionsort as sc
from DISClib.Algorithms.Sorting import quicksort as sd
from DISClib.Algorithms.Sorting import mergesort as se

assert cf
import time 
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(listType: int):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para el titulo del video,
    una lista vacia para el canal que lo creó, una lista vacia para la fecha de tendencia, 
    una lista vacia para el país, una lista vacia para la cantidad de vistas y una lista vacia para
    la cantidad de likes y dislikes. Finalmente, crea una lista de las categorías mostrando su id y su nombre.
    Retorna el catalogo inicializado. 
    """
    catalog = {'videos': None}        

    if listType == 1:
        eda = 'ARRAY_LIST'

    elif listType == 2:
        eda = 'LINKED_LIST'
        
    catalog['videos'] = lt.newList(datastructure=eda)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)

    """
    #TODO
    # Se obtienen las categorias del video
    authors = book['authors'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        addBookAuthor(catalog, author.strip(), book)
        """

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los likes de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'likes'
    video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (int(video1['likes']) < int(video2['likes']))

# Funciones de ordenamiento

def sortVideos(catalog, size, tisa):

    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()

    if tisa == 1: 
        sorted_list = sb.sort(sub_list, cmpVideosByLikes)
    elif tisa == 2:
        sorted_list = sc.sort(sub_list, cmpVideosByLikes)
    elif tisa == 3:
        sorted_list = sa.sort(sub_list, cmpVideosByLikes)
    elif tisa == 4:
        sorted_list = sd.sort(sub_list, cmpVideosByLikes)
    elif tisa == 5:
        sorted_list = se.sort(sub_list, cmpVideosByLikes)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    

    return elapsed_time_mseg, sorted_list

