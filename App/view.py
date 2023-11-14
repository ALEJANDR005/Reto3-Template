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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
from datetime import datetime as dt

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    return controller.new_controller()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")

def archivo()->str:
    input_file_size = int(input("Seleccione el tamaño del archivo: \n 1-5% \n 2-10% \n 3-20% \n 4-30% \n 5-50% \n 6-80% \n 7-large \n 8-small \n"))
    tamanio = ""
    if input_file_size == 1:
        tamanio = "-5pct.csv"
    elif input_file_size == 2:
        tamanio = "-10pct.csv"
    elif input_file_size == 3:
        tamanio = "-20pct.csv"
    elif input_file_size == 4:
        tamanio = "-30pct.csv"
    elif input_file_size == 5:
        tamanio = "-50pct.csv"
    elif input_file_size == 6:
        tamanio = "-80pct.csv"
    elif input_file_size == 7:
        tamanio = "-large.csv"
    elif input_file_size == 8:
        tamanio = "-small.csv"
    return tamanio

def load_data(control, tamanio):
    """
    Carga los datos
    """
    temblores = "temblores-utf8"+tamanio
    result = controller.load_data(control, temblores)
    print("---- EATHQUAKES RESULTS ----")
    return result

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    initial_date = dt.strptime(input("Ingrese la fecha inicial(YYYY-mm-dd): "),"%Y-%m-%d").date()
    final_date = dt.strptime(input("Ingrese la fecha final(YYYY-mm-dd): "),"%Y-%m-%d").date()
    result, total = controller.req_1(control, initial_date, final_date)
    
    print("============= REQ No. 1 Results ============")
    print("Total de eventos encontrados: ", total)
    print(tabulate(lt.iterator(result), headers="keys", tablefmt="grid"))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    print("============= REQ No. 2 Inputs ============")

    lower = float(input("Ingrese el limite inferior: "))
    upper = float(input("Ingrese el limite superior: "))
    result, contador, time = controller.req_2(control, lower, upper)
    
    print("============= REQ No. 2 Results ============")
    print("Total de eventos encontrados:",contador)
    print(tabulate(lt.iterator(result), headers="keys", tablefmt="grid"))
    print("El tiempo en ms es",time)

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    print("============= REQ No. 5 Inputs ============")

    depth = float(input("Ingrese la profundida minima: "))
    nst = float(input("Ingrese el nst minimo: "))
    result, contador, time = controller.req_5(control, depth, nst)
    
    print("============= REQ No. 5 Results ============")
    print("Total de eventos encontrados:",contador)
    print("El tiempo en ms es",time)
    print(tabulate(lt.iterator(result), headers="keys", tablefmt="grid"))

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            control = new_controller()
            print("Cargando información de los archivos ....\n")
            tamanio = archivo()
            size, lista = load_data(control, tamanio)
            print(size)
            print(tabulate(lt.iterator(lista), headers="keys", tablefmt="grid"))

        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

