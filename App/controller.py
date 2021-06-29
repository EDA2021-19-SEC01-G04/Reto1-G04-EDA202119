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
 """

import config as cf
import model
import csv
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sb
from DISClib.Algorithms.Sorting import insertionsort as sc
from DISClib.Algorithms.Sorting import quicksort as sd
from DISClib.Algorithms.Sorting import mergesort as se


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(listType):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(listType)
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)


def loadVideos(catalog):
    """
    Carga los videos del archivo.  
    """
    videosFile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosFile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    
    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'))
    for category in input_file:
        model.addCategory(catalog, category) 


# Funciones de ordenamiento

def sortVideos(catalog, size, tisa):
    """
    Ordena los videos por cantidad de likes
    """
    return model.sortVideos(catalog, size, tisa)

# Funciones de consulta sobre el catálogo

def getBestVideos(catalog, number, category_name, country):
    
    category = model.getCategoryByName(catalog, category_name)
    top = model.getBestVideos(catalog, number, category["id"], country)

    return top

def getMostTrendingVideoByCountry(catalog, pais):
    filteredVideos = model.filterByCountry(catalog, pais)
    filteredVideos = model.filterByRatioLikesDislikes(filteredVideos, 10)


    return model.getMostTrendingVideo(filteredVideos)

def getMostTrendingVideoByCategory (catalog, category):

    category = model.getCategoryByName(catalog, category)

    filteredVideos = model.filterByCategory(catalog, category['id'])
    filteredVideos = model.filterByRatioLikesDislikes(filteredVideos, 20)


    return model.getMostTrendingVideo(filteredVideos)

def getMostComentedVideosByCountryTag(catalog, pais, tag, num):

    top = model.getMostCommentedVideos(catalog, pais, tag, num)

    return top

