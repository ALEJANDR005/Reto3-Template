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

import matplotlib.pyplot as plt
import math 
import config as cf
from time import strptime
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
import datetime as dt
from time import strftime
from tabulate import tabulate

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
    earthquakes = {"temblores": None,
                    "time": None,
                    "mag": None,
                    "depth": None,
                    "sig": None,
                    "gap": None,
                    "nst" : None,
                    }
    
    earthquakes["temblores"] = lt.newList("ARRAY_LIST")
    earthquakes["time"] = om.newMap(omaptype="RBT", cmpfunction=cmpDates)
    earthquakes["mag"] = om.newMap(omaptype="RBT", cmpfunction=cmpMag)
    earthquakes["depth"] = om.newMap(omaptype="RBT", cmpfunction=cmpDepth)
    earthquakes["sig"] = om.newMap(omaptype="RBT", cmpfunction=cmpSig)
    earthquakes["gap"] = om.newMap(omaptype="RBT", cmpfunction=cmpGap)

    return earthquakes


# Funciones para agregar informacion al modelo

def add_temblores_fechas(earthquakes, temblores):
    """
    Función para agregar fechas al arbol.
    """
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

def add_sig(earthquakes, temblores):
    """
    Función para agregar magnitudes al arbol.
    """
    sigs = earthquakes["sig"]
    if not om.contains(sigs,temblores["sig"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(sigs, temblores["sig"], lista)
    else:
        pair = om.get(sigs, temblores["sig"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(sigs, temblores["sig"], lista)
   
    return sigs

def add_gap(earthquakes, temblores):
    """
    Función para agregar magnitudes al arbol.
    """
    gaps = earthquakes["gap"]
    if not om.contains(gaps,temblores["gap"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(gaps, temblores["gap"], lista)
    else:
        pair = om.get(gaps, temblores["gap"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(gaps, temblores["gap"], lista)
   
    return gaps

def add_depth(earthquakes, temblores):
    """
    Función para agregar magnitudes al arbol.
    """
    magnitudes = earthquakes["depth"]
    if not om.contains(magnitudes,temblores["depth"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(magnitudes, temblores["depth"], lista)
    else:
        pair = om.get(magnitudes, temblores["depth"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(magnitudes, temblores["depth"], lista)
   
    return magnitudes

def add_sig(earthquakes, temblores):
    """
    Función para agregar magnitudes al arbol.
    """
    magnitudes = earthquakes["sig"]
    if not om.contains(magnitudes,temblores["sig"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(magnitudes, temblores["sig"], lista)
    else:
        pair = om.get(magnitudes, temblores["sig"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(magnitudes, temblores["sig"], lista)
   
    return magnitudes

def add_earthquakes(earthquakes, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    data_filtrada = filtrar(data["code"], data["time"], data["lat"], data["long"], data["mag"], data["nst"], data["title"], data["depth"], data["felt"], data["cdi"], data["mmi"], data["tsunami"] , data["sig"] , data["gap"])
    lt.addLast(earthquakes["temblores"], data_filtrada)
    add_mag(earthquakes, data_filtrada)
    add_temblores_fechas(earthquakes, data_filtrada)
    add_depth(earthquakes, data_filtrada)
    add_sig(earthquakes, data_filtrada)
    add_gap(earthquakes, data_filtrada)

def filtrar(code, time, lat, long, mag, nst, title,depth,felt, cdi, mmi, tsunami , sig , gap):
    resp = {
        "code": code,
        "time": time,
        "lat": lat,
        "long": long,
        "sig" : sig,
        "mag": float(mag),
        "nst": float(nst) if not nst in[None,"", " "] else "Unknown",
        "title": title,
        "depth": float(depth),
        "felt": felt if not felt in [None, "", " "] else "Unknown",
        "cdi": cdi if not cdi in [None, "", " "] else "Unknown",
        "mmi": mmi if not mmi in [None, "", " "] else "Unknown",
        "tsunami": False if tsunami == "0" else True, 
        "sig" : float(sig),
        "gap" : float(gap) if not gap in [None, "", " "] else "Unknown"
    }
    
    return resp

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

def temblores_size(earthquake):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(earthquake["temblores"])


def req_1(earthquakes, initial, final):
    """
    Función que soluciona el requerimiento 1
    """
    
    treeDates = earthquakes["time"]
    valores = om.values(treeDates, initial, final)
    llaves = om.keys(treeDates, initial, final)
    lt.iterator(valores)
    resp = lt.newList("ARRAY_LIST")
    
    i=1
    while i<= lt.size(llaves):
        key = lt.getElement(llaves, i)
        value = lt.getElement(valores, i)
        dic = { "time": key,       
                "events": lt.size(value),    
                "details": tabulate(lt.iterator(value),headers="keys",tablefmt="grid")
                }
        lt.addLast(resp, dic)
        i+=1
        
    return resp, lt.size(llaves)


def req_2(earthquakes, inferior, superior):
    """
    Función que soluciona el requerimiento 2
    """
    
    mag_map = earthquakes["mag"]
    values = om.values(mag_map, inferior, superior)
    keys = om.keys(mag_map, inferior, superior)
    lt.iterator(values)
    answer = lt.newList("ARRAY_LIST")
    
    i=1
    
    while i<= lt.size(keys):
        key = lt.getElement(keys,i)
        value = lt.getElement(values,i)
        value3 = get3_normal_req1_2(value)
        dic = {"mag":key,
               "events": lt.size(value),
               "details": tabulate(lt.iterator(value3), headers="keys", tablefmt="grid",maxcolwidths=[None, None, None, None, None, None, None, 20, None, None, None, None, None])
               }
        lt.addLast(answer, dic)
        i+=1
        
    return get3(answer), lt.size(keys)



def req_3(earthquakes, min_depth, min_mag):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    depth_arbol = earthquakes["depth"]
    max_depth = om.maxKey(depth_arbol)
    keys = om.keys(depth_arbol, min_depth, max_depth)  
    answer = lt.newList("ARRAY_LIST")
    contador = 0
    for depth_key in lt.iterator(keys):        
        element_depth = om.get(depth_arbol, depth_key)
        value_element = element_depth["value"]
        elements = value_element["elements"]
        for element in elements:
            mag = element["mag"]
            if mag >= min_mag:
                lt.addLast(answer, element)
                contador+=1
    answer_sorted = sorted(answer['elements'], key=lambda x: x['time'], reverse=True)

    final = lt.newList("ARRAY_LIST")
    for data in (answer_sorted):
        keys = data.keys()
        table = tabulate([data.values()], headers=keys, tablefmt="grid", maxcolwidths=[None, None, None, None, None, None, 20, None, None, None, None, None])

        dic = {"time": data["time"],
               "events" :1,
               "details" : table}
        lt.addLast(final, dic)
    final3 = get10_req3(final)
    return final3, contador



def req_4(earthquakes, sig_min , gap_max):
    """
    Función que soluciona el requerimiento 4
    
    """
    sig_ar = earthquakes["sig"]
    max_sig = om.maxKey(sig_ar)
    keys = om.keys(sig_ar, sig_min, max_sig)
    answer = lt.newList("ARRAY_LIST")
    contador = 0

    all_elements = []
    for sig_key in lt.iterator(keys):
        element_sig = om.get(sig_ar, sig_key)
        value_element = element_sig["value"]
        elements = value_element["elements"]
        for element in elements:
            gap = element["gap"]
            if gap == "Unknown":
                gap = 0
            if gap <= gap_max:
                all_elements.append(element)
                contador += 1

    all_elements_sorted = sorted(all_elements, key=lambda x: x['time'], reverse=True)
    first_15_elements = all_elements_sorted[:15]
    selected_elements = first_15_elements[:3] + first_15_elements[-3:]

    final = lt.newList("ARRAY_LIST")
    for data in selected_elements:
        keys = data.keys()
        table = tabulate([data.values()], headers=keys, tablefmt="grid", maxcolwidths=[None, None, None, None, None, None, 20, None, None, None, None, None])

        dic = {"time": data["time"],
               "events": 1,
               "details": table}
        lt.addLast(final, dic)

    final3 = get3(final)
    return final3, contador
    
    
                
                    
        
    
    


def req_5(earthquakes, min_depth, min_nst):
    depth_arbol = earthquakes["depth"]
    max_depth = om.maxKey(depth_arbol)
    keys = om.keys(depth_arbol, min_depth, max_depth)  
    answer = lt.newList("ARRAY_LIST")
    contador = 0
    for depth_key in lt.iterator(keys):        
        element_depth = om.get(depth_arbol, depth_key)
        value_element = element_depth["value"]
        elements = value_element["elements"]
        for element in elements:
            nst = element["nst"]
            if nst == "Unknown":
                nst = 0
            if nst >= min_nst:
                lt.addLast(answer, element)
                contador+=1
    answer_sorted = sorted(answer['elements'], key=lambda x: x['time'], reverse=True)
    if len(answer_sorted)>20:
        answer_filtered = answer_sorted[:20]
    else:
        answer_filtered = answer_sorted
    final = lt.newList("ARRAY_LIST")
    for data in (answer_filtered):
        keys = data.keys()
        table = tabulate([data.values()], headers=keys, tablefmt="grid", maxcolwidths=[None, None, None, None, None, None, None, 20, None, None, None, None, None])

        dic = {"time": data["time"],
               "events" :1,
               "details" : table}
        lt.addLast(final, dic)
    final3 = get3(final)
    return final3, contador


def req_6(earthquakes, year, lat, long, radius, n_events):
    """
    Función que soluciona el requerimiento 6
    """
    treeDates = earthquakes["time"]
    initial = "{year}-01-01T00:00".format(year)
    final = "{year}-12-30T00:00".format(year)

    valores = om.values(treeDates, initial, final)
    llaves = om.keys(treeDates, initial, final)
    lt.iterator(valores)
    resp = lt.newList("ARRAY_LIST")
    
    i=1
    while i<= lt.size(llaves):
        key = lt.getElement(llaves, i)
        value = lt.getElement(valores, i)
        dic = { "time": key,       
                "events": lt.size(value),    
                "details": tabulate(lt.iterator(value),headers="keys",tablefmt="grid")
                }
        lt.addLast(resp, dic)
        i =+1
    return resp
    
def haversine(D, 𝜙1, 𝜙2, 𝜆1, 𝜆2, 𝜇𝐸=6371):
    """
    Calcula la distancia entre dos puntos en la superficie de la Tierra utilizando la fórmula de Haversine.

    :param D: Distancia entre los dos puntos en kilómetros.
    :param 𝜙1: Latitud del primer punto en radianes.
    :param 𝜙2: Latitud del segundo punto en radianes.
    :param 𝜆1: Longitud del primer punto en radianes.
    :param 𝜆2: Longitud del segundo punto en radianes.
    :param 𝜇𝐸: Radio de la Tierra en kilómetros (por defecto, 6371 km).
    :return: Distancia calculada en kilómetros.
    """
    sin_term = math.sin((𝜙2 - 𝜙1) / 2) ** 2
    cos_term = math.cos(𝜙1) * math.cos(𝜙2) * math.sin((𝜆2 - 𝜆1) / 2) ** 2
    distance = 2 * math.asin(math.sqrt(sin_term + cos_term)) * 𝜇𝐸
    return distance

def req_7(earthquakes , año , titulo , propiedad , bins):
    """
    Función que soluciona el requerimiento 7
    """
    propiedades = earthquakes[propiedad] 
    max_prop = om.maxKey(propiedades)
    min_prop = om.minKey(propiedades)
    propiedades_value = om.values(propiedades , min_prop , max_prop)
    
    eventos_seleccionados = [evento for evento in earthquakes if evento["time"][:4] == año and evento["title"] == titulo]


    if propiedad not in eventos_seleccionados[0]:
        return {"error": "La propiedad especificada no existe en los eventos seleccionados."}


    valores_propiedad = [evento[propiedad] for evento in eventos_seleccionados if evento[propiedad] != "Desconocido"]


    conteo, bordes, _ = plt.hist(valores_propiedad, bins=bins, edgecolor='black', alpha=0.7)
    plt.close()


    eventos_seleccionados = eventos_seleccionados[:3] + eventos_seleccionados[-3:]


    min_valor = min(valores_propiedad, default="Desconocido")
    max_valor = max(valores_propiedad, default="Desconocido")

    resultado = {
        'num_eventos_anuales': len(eventos_seleccionados),
        'num_eventos_histograma': len(valores_propiedad),
        'min_valor': min_valor,
        'max_valor': max_valor,
        'histograma': {'conteo': conteo.tolist(), 'bordes': bordes.tolist()},
        'eventos_seleccionados': eventos_seleccionados
    }

    return resultado
    
    
    


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
    
def cmpDates_req5(data1, data2):
    """
    Compara dos fechas
    """
    date1 = data1["time"]
    date2 = data2["time"]
    
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
    
def cmpDepth(depth1, depth2):
    """
    Compara dos fechas
    """
    if (depth1 == depth2):
        return 0
    elif (depth1 > depth2):
        return 1
    else:
        return -1
def cmpGap(gap1, gap2):
    """
    Compara dos fechas
    """
    if gap1 =="Unknown":
        gap1 = 0
    if gap2 =="Unknown":
        gap2 = 0
    
    if (gap1 == gap2):
        return 0
    elif (gap1 > gap2):
        return 1
    else:
        return -1    
    
def cmpSig(sig1, sig2):
    """
    Compara dos fechas
    """
    if (sig1 == sig2):
        return 0
    elif (sig1 > sig2):
        return 1
    else:
        return -1
    
def cmpNst(nst1, nst2):
    
    if nst1 == "Unknown":
        nst1 = 0
    if nst2 == "Unknown":
        nst2 = 0
        
    if (nst1 == nst2):
        return 0
    elif (nst1 > nst2):
        return 1
    else:
        return -1
def cmpSig(sig1, sig2):
    if (sig1 == sig2):
        return 0
    elif (sig1 > sig2):
        return 1
    else:
        return -1
def get5(lista):
    sublist = lt.newList("ARRAY_LIST")
    for x in range(0,5):
        element = lt.getElement(lista, x)
        lt.addLast(sublist, element)
    for x in range((lt.size(lista)-5),(lt.size(lista))):
        element = lt.getElement(lista, x)
        lt.addLast(sublist, element)
    return sublist 

def get3(lista):
    if lt.size(lista) > 6:
        sublist = lt.newList("ARRAY_LIST")
        for x in range(1,4):
            element = lt.getElement(lista, x)
            lt.addLast(sublist, element)
        for x in range((lt.size(lista)-3),(lt.size(lista))):
            element = lt.getElement(lista, x)
            lt.addLast(sublist, element)
    else:
        sublist = lista
    return sublist 

def get3_normal(lista):
    if len(lista) > 6:
        sublist = lt.newList("ARRAY_LIST")
        primeros3 = lista[:3]
        lt.addLast(sublist, primeros3)
        ultimos3 = lista[-3:]
        lt.addLast(sublist, ultimos3)
    else:
        sublist = lista
    return sublist 


def get3_normal_req1_2(lista):
    if lt.size(lista) > 3:
        sublist = lt.newList("ARRAY_LIST")
        for x in range(1,4):
            element = lt.getElement(lista, x)
            lt.addLast(sublist, element)
    else:
        sublist = lista
    return sublist 

def mag(earthquakes):
    return earthquakes["mag"]

def get10_req3(lista):
    if lt.size(lista) > 10:
        sublist = lt.newList("ARRAY_LIST")
       
        for x in range((lt.size(lista)-10),(lt.size(lista))):
            element = lt.getElement(lista, x)
            lt.addLast(sublist, element)
    else:
        sublist = lista
    return sublist 