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
from datetime import datetime
import config as cf
import model
import time
import csv
import tracemalloc
from datetime import datetime as dt
import csv
import sys
import os
"""
Ayuda para la lectura de los archivos.
"""
csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control, ruta):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    earthquakes = control["model"]
    eathquakesFile = os.path.join(cf.data_dir+"/earthquakes", ruta)
    inputEarthquakesFile = csv.DictReader(open(eathquakesFile, encoding="utf-8"))
    for temblor in inputEarthquakesFile:
        tiempo_str = temblor["time"]
        tiempo_datetime = datetime.strptime(tiempo_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        tiempo_date = tiempo_datetime.date()
        temblor["time"] = tiempo_date
        model.add_earthquakes(earthquakes, temblor)
    sizeEarthquakes= model.temblores_size(earthquakes)
    return sizeEarthquakes, model.get5(earthquakes["temblores"])

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, initial, final):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    temblores, contador = model.req_1(control["model"], initial, final)
    return model.get3(temblores), contador


def req_2(control, low, high):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time = time.time()
    temblores, contador = model.req_2(control["model"], low, high)
    end_time = time.time()
    execution_time = end_time - start_time
    return temblores, contador, execution_time

def req_3(control, min_depth, min_mag):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = time.time()
    result, contador = model.req_5(control["model"], min_depth, min_mag)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, contador, execution_time


def req_4(control , sig_min , gap_max):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = time.time()
    temblores, contador = model.req_4(control["model"], sig_min, gap_max)
    end_time = time.time()
    execution_time = end_time - start_time
    return temblores, contador, execution_time


def req_5(control, depth, nst):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = time.time()
    result, contador = model.req_5(control["model"], depth, nst)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, contador, execution_time


def req_6(control, year, dlat, dlon):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = time.time()
    result,  = model.req_5(control["model"], year, dlat, dlon)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def req_7(control ,  año , titulo , propiedad , bins):
    """
    Retorna el resultado del requerimiento 7
    """
    start_time = time.time()
    temblores = model.req_7(control["model"], año , titulo , propiedad , bins)
    end_time = time.time()
    execution_time = end_time - start_time
    return temblores,execution_time


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
def mag(control):
    return model.mag(control["model"])