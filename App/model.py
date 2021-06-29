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
from datetime import datetime
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(listType: int):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos. 
    """
    catalog = {'videos': None,'categories': None}    

    if listType == 1:
        eda = 'ARRAY_LIST'

    elif listType == 2:
        eda = 'LINKED_LIST'
        
    catalog['videos'] = lt.newList(datastructure = eda)
    catalog['categories'] = lt.newList(datastructure = eda)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    """
    Adiciona una categoria a la lista de categorias
    """
    t = newCategory(category['name'], category['id'])
    lt.addLast(catalog['categories'], t)
    
# Funciones para creacion de datos

def newCategory(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    category = {'name': '', 'id': ''}
    category['name'] = name
    category['id'] = id
    return category

# Funciones de consulta

def filterVideosByCountryAndCategory(catalog, category_id, country):
    """
    Retorna una sublista con los videos que cumplan el pais y la categoria
    """
    videos = lt.iterator(catalog["videos"])
    filteredVideos = lt.newList()

    for video in videos:
        if video["category_id"] == category_id and video["country"] == country:
            lt.addLast(filteredVideos, video)
    
    return filteredVideos 

def filterByCountry (catalog, country):

    videos = lt.iterator(catalog['videos'])
    filteredByCountry = lt.newList()

    for video in videos:
        if video['country'] == country:
            lt.addLast(filteredByCountry, video)
    
    return filteredByCountry

def filterByTagAndCountry (catalog, tag, country):

    videos = lt.iterator(catalog['videos'])
    filteredByTagAndCountry = lt.newList()

    for video in videos:
        if tag in video['tags'] and video["country"] == country:
            lt.addLast(filteredByTagAndCountry, video)
    
    return filteredByTagAndCountry    

def filterByCategory (catalog, category):

    videos = lt.iterator(catalog['videos'])
    filteredByCategory = lt.newList()

    for video in videos:
        if video['category_id'] == category:
            lt.addLast(filteredByCategory, video)
    
    return filteredByCategory


def filterByRatioLikesDislikes (listaFiltrada, minratio):

    filteredByRatio = lt.newList()

    for video in lt.iterator(listaFiltrada):
        ratio = int(video['likes'])/max(1,int(video['dislikes']))

        if (ratio > minratio):
            lt.addLast(filteredByRatio, video)
    
    return filteredByRatio





def getCategoryByName(catalog, name):

    categories = lt.iterator(catalog["categories"])

    for category in categories:
        if category["name"] == name:
            return category        

def getMostCommentedVideos(catalog, country, tag, num):
    
    videos = filterByTagAndCountry(catalog, tag, country)

    if lt.size(videos) > 0:
        sortedVideos = se.sort(videos, cmpVideosByComments)
        defVideos = lt.newList()

        for counter in range(1, min(num, lt.size(sortedVideos)+1)):

            video = lt.getElement(sortedVideos, counter)
            lt.addLast(defVideos, video)
        
        return defVideos
    
    else:
        return None



def getBestVideos(catalog, number, category_id, country):
    """
    Retorna los mejores videos
    """
    videos = filterVideosByCountryAndCategory(catalog, category_id, country)

    if lt.size(videos) > 0:
        sortedVideos = se.sort(videos, cmpVideosByLikes)
        defVideos = lt.newList()

        for counter in range(1, min(number, lt.size(sortedVideos)+1)):

            video = lt.getElement(sortedVideos, counter)
            lt.addLast(defVideos, video)
        
        return defVideos
    
    else:
        return None

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los likes de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'likes'
    video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (int(video1['likes']) > int(video2['likes']))

def cmpVideosByComments(video1, video2):

    return (int(video1['comment_count']) > int(video2['comment_count']))


def getDeltaDays(video):
    videoTrendingDate = video["trending_date"]
    videoTrendingDate = datetime.strptime(videoTrendingDate, '%y.%d.%m')

    videoPublishDate = video["publish_time"]
    videoPublishDate = videoPublishDate.split("T")[0]
    videoPublishDate = datetime.strptime(videoPublishDate, '%Y-%m-%d')

    videoDeltaDays = videoTrendingDate - videoPublishDate

    return videoDeltaDays


def cmpVideosByTrendDate(video1, video2):
    video1DeltaDays = getDeltaDays(video1)
    video2DeltaDays = getDeltaDays(video2)

    return video1DeltaDays > video2DeltaDays


def getMostTrendingVideo(lista_videos):

    videos_ordenados = se.sort(lista_videos, cmpVideosByTrendDate)
    video_mas_trending = lt.firstElement(videos_ordenados)
    
    return video_mas_trending, getDeltaDays(video_mas_trending)
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
    


