﻿"""
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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from datetime import datetime as dt

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    earthquakes = {"mag": None,
                "place": None,
                "time": None,
                }

    earthquakes["mag"] = om.newMap(omaptype="RBT", cmpfunction=cmpMag)
    earthquakes["place"] = lt.newList("ARRAY_LIST")
    earthquakes["time"] = om.newMap(omaptype="RBT", cmpfunction=cmpDates)
    return earthquakes


# Funciones para agregar informacion al modelo

def add_temblores_fechas(earthquakes, temblores):
    """
    Función para agregar fechas al arbol.
    """
    #TODO: Crear la función para agregar elementos a una lista
    fechas = earthquakes["time"]
    if not om.contains(fechas,temblores["time"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(fechas, temblores["time"], lista)
    else:
        pair = om.get(fechas, temblores["time"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(fechas, temblores["time"], lista)
   
    return fechas
        
def add_mag(earthquakes, temblores):
    """
    Función para agregar magnitudes al arbol.
    """
    magnitudes = earthquakes["mag"]
    if not om.contains(magnitudes,temblores["mag"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(magnitudes, temblores["mag"], lista)
    else:
        pair = om.get(magnitudes, temblores["mag"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(magnitudes, temblores["mag"], lista)
   
    return magnitudes

def add_earthquakes(earthquakes, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    add_mag(earthquakes, data)
    add_temblores_fechas(earthquakes, data)

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def timeSize(earthquakes):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(earthquakes["time"])

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(earthquakes, initial, final):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    treeDates = earthquakes["time"]
    keys = om.values(treeDates, initial, final)
    datos = lt.iterator(keys)
    lista = []
    contador = 0
    for each in datos:
        if each not in lista:
            lista.append(each)
            contador += 1
        
    return keys, contador


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

    
def cmpDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def cmpMag(mag1, mag2):
    """
    Compara dos fechas
    """
    if (mag1 == mag2):
        return 0
    elif (mag1 > mag2):
        return 1
    else:
        return -1