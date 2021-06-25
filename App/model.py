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
assert cf

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
    catalog = {'videos': None,
               'title': None,
               'cannel_title': None,
               'trending_date': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None}          

    if listType == 1:

        eda = 'ARRAY_LIST'

    elif listType == 2:

         eda = 'LINKED_LIST'
        
    catalog['videos'] = lt.newList()
    
    catalog['title'] = lt.newList(eda)

    catalog['cannel_title'] = lt.newList(eda)

    catalog['trending_date'] = lt.newList(eda)

    catalog['country'] = lt.newList(eda)

    catalog['views'] = lt.newList(eda)

    catalog['likes'] = lt.newList(eda)

    catalog['dislikes'] = lt.newList(eda)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo (catalog, video):
    lt.addLast(catalog['videos'], video)

    """
    authors = book['authors'].split(",")

    for author in authors:
        addBookAuthor(catalog, author.strip(), book)
        """
def addTitle(catalog, title):
    """
    Adiciona un titulo a la lista de tags
    """
    t = newTitle(title['tag_id'], title['goodreads_book_id'])
    lt.addLast(catalog['book_tags'], t)


        

# Funciones para creacion de datos

def newTitle(title, videos):
    """
    Esta estructura crea una relación entre un titulo y
    los videos que han sido marcados con dicho titulo.
    """
    titulo = {'title': title, 'videos': videos}
    return titulo

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento