"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sb
from DISClib.Algorithms.Sorting import insertionsort as sc
from DISClib.Algorithms.Sorting import quicksort as sd
from DISClib.Algorithms.Sorting import mergesort as se


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit = 1000
sys.setrecursionlimit(default_limit*1000000)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Seleccionar el tipo de algoritmo de ordenamiento con el cual organizar los datos")
    print("3- Consultar el Top de videos con más likes")
    print("4- Consultar el video con más días de tendencia en un determinado país")
    print("5- Consultar el video con más días de tendencia en una determinada categoría")
    print("6- Consultar el top de videos con mas comentarios segun tag y país")

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        
        print("Seleccione la opción con el tipo de lista que desea para cargar el catálogo de videos: ")
        print("1. Array List ")
        print("2. Linked List ")
        listType = int(input("Elección: "))
        catalog = controller.initCatalog(listType)
        print("Cargando información de los archivos ....")
        loadData(catalog)
        print("El total de registro de videos cargados es: " +str(lt.size(catalog['videos'])))

        firstVideo = lt.firstElement(catalog['videos']) 
        print ("Información sobre el primer video cargado: ")
        print(" -> title: ", firstVideo["title"])
        print(" -> cannel title: ", firstVideo["channel_title"])
        print(" -> trending date: ", firstVideo["trending_date"])
        print(" -> country: ", firstVideo["country"])
        print(" -> views: ", firstVideo["views"])
        print(" -> likes: ", firstVideo["likes"])
        print(" -> dislikes: ", firstVideo["dislikes"])

        print("Las categorias existentes son: ")
        print("|   id    |    category")
        for category in catalog["categories"]["elements"]:
            print("   |   " + category["id"] + "   |   " + category["name"])       


    elif int(inputs[0]) == 2:
        print("Seleccione la opción con el tipo de algoritmo de ordenamiento con el cual organizar los datos: ")
        print("1- Selection")
        print("2- insertion")
        print("3- shell")
        print("4- Quick")
        print("5- Merge")
        tisa = input("Elección: ")
        size = int(input("Indique tamaño de la muestra: "))
        result = controller.sortVideos(catalog, int(size), int(tisa))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        
    elif int(inputs[0]) == 3:
        categoria = input("ingrese el nombre de la categoria: ")
        pais = input("ingrese el pais del video: ")
        n = int(input("¿Qué TOP desea consultar?: "))


        mejores_videos = controller.getBestVideos(catalog, n, categoria, pais)
        
        if mejores_videos == None:
            print("No se encuentra un video con las  características solicitadas")
        else:
            if lt.size(mejores_videos) < n:
                print("El top solicitado es mayor a la cantidad total de videos encontrados. Sin embargo... ")
           
            print("Los videos con más likes en el país", pais, "y en la categoría", categoria, "son: ")
            indice = 1
            for video in lt.iterator(mejores_videos):

                print(str(indice), "-- Trending date: ", video["trending_date"])
                print("Title:", video['title'])
                print("Channel title:", video['channel_title'])              
                print("Publish time:", video['publish_time'])
                print("Views:", video['views'])
                print("Likes:", video['likes'])
                print("Dislikes:", video['dislikes'])

                indice += 1
    
    elif int(inputs[0]) == 4:
        pais = input("Ingrese el país sobre el cual desea hacer la consulta: ")
        
        bestVideoTuple = controller.getMostTrendingVideoByCountry(catalog, pais)
        bestVideo = bestVideoTuple[0]
        numeroDias = bestVideoTuple[1]

        print("El video con más días en tendencia en", pais, "es: ")
        print("title:  ", bestVideo['title'])
        print("channel title:  ", bestVideo['channel_title'])
        print("country: ", bestVideo['country'])
        print("ratio likes/dislikes", str(float(round(int(bestVideo['likes'])/int(bestVideo['dislikes']),2))))
        print("Número de días: ", numeroDias )
    
    elif int(inputs[0]) == 5:

        category = input("ingrese la categoria sobre la cual desea hacer la colsulta: " )

        bestVideoTuple = controller.getMostTrendingVideoByCategory(catalog, category)
        bestVideo = bestVideoTuple[0]
        numeroDias = bestVideoTuple[1]

        print("El video con más días en tendencia en la categoría", category, "es: ")
        print("title:  ", bestVideo['title'])
        print("channel title:  ", bestVideo['channel_title'])
        print("country: ", bestVideo['country'])
        print("ratio likes/dislikes", str(float(round(int(bestVideo['likes'])/int(bestVideo['dislikes']),2))))
        print("Número de días: ", numeroDias )

    elif int(inputs[0]) == 6:
        tag = input("ingrese el tag que desea buscar: ")
        pais = input("ingrese el pais del video: ")
        num = int(input("¿Qué TOP desea consultar?: "))


        masComentados = controller.getMostComentedVideosByCountryTag(catalog, pais, tag, num)
        
        if masComentados == None:
            print("No se encuentran videos con las  características solicitadas")
        else:
            if lt.size(masComentados) < num:
                print("El top solicitado es mayor a la cantidad total de videos encontrados. Sin embargo... ")
           
            print("Los videos con más comentarios en el país", pais, "y con el tag", tag, "son: ")
            indice = 1
            for video in lt.iterator(masComentados):
                print("----- top", indice, "-----")
                print("Title:", video['title'])
                print("Channel title:", video['channel_title'])              
                print("Publish time:", video['publish_time'])
                print("Views:", video['views'])
                print("Likes:", video['likes'])
                print("Dislikes:", video['dislikes'])
                print("Comment count:", video['comment_count'])
                print("Tags:", video['tags'])

                indice += 1

                

    else:
        sys.exit(0)
sys.exit(0) 

