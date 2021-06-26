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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar libros por likes")

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


    elif int(inputs[0]) == 2:
        print("Seleccione la opción con el tipo de algoritmo de ordenamiento iterativo con el cual organizar los datos: ")
        print("1- Selection")
        print("2- insertion")
        print("3- shell")
        tisa = input("Elección: ")
        size = int(input("Indique tamaño de la muestra: "))
        result = controller.sortVideos(catalog, int(size), int(tisa))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        


    else:
        sys.exit(0)
sys.exit(0)
