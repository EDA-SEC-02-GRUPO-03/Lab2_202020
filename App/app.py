"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import selectionsort as sel 
from Sorting import insertionsort as ins 
from Sorting import shellsort as sh
from time import process_time 


def loadCSVFile (file1,file2, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst1 = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst1 = lt.newList() #Usando implementacion linkedlist
    lst2 = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst2 = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivos ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file1, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst1,row)
        with open(file2, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst2,row)

    except:
        print("Hubo un error con la carga de los archivos")

    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return (lst1,lst2) 

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print('5- Req. 1: Buenas películas de un director')
    print('6- Req. 2: Ranking de Películas')
    print('7- Req. 5: Películas por género')
    print("0- Salir")


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        lst
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def req1(lst1, lst2, criteria1, column1, criteria2, column2):

    if lst1['size'] == 0 or lst2['size'] == 0:
        print ('Lista vacía')
    else:
        t1_start = process_time()
        counter = 0
        iterator1 = it.newIterator(lst1)
        i = 0
        positions = []
        while  it.hasNext(iterator1):
            element = it.next(iterator1)
            if criteria1.lower() in element[column1].lower(): #filtrar por palabra clave 
                positions.append(i)
            i+=1
        for i in positions:
            element = lt.getElement(lst2 ,i)
            if float(element[column2]) >= float(criteria2):
                counter += 1            
    t1_stop = process_time()
    print('EL tiempo es de ', t1_stop-t1_start, ' segundos')
    return counter

def lessfunction(element1, element2, criteria):
    if float(element1[criteria]) < float(element2[criteria]):
        return True
    return False

def greaterfunction(element1, element2, criteria):
    if float(element1[criteria]) > float(element2[criteria]):
        return True
    return False

def req2 (lst, function, criteria, n):
    
    t1_start = process_time()
    result = []
    sh.shellSort(lst, function, criteria)
    #sel.selectionSort(lst, function, criteria)       
    #ins.insertionSort(lst,function,criteria)

    for i in range(n+1):
        result.append(lt.getElement(lst, i))
        result[i] = (result[i]['title'],result[i][criteria])
    del result[0]
    t1_stop = process_time()
    print('El tiempo fue de ', t1_stop-t1_start, ' segundos')
    return result

def req5(lst, criteria1, column1, column2, column3):
    if lst['size'] == 0:
        print ('Lista vacía')
    else:
        t1_start = process_time()
        iterator1 = it.newIterator(lst)
        nombres = []
        votos = []
        counter = 0
        while  it.hasNext(iterator1):
            element = it.next(iterator1)
            if criteria1.lower() in element[column1].lower(): #filtrar por palabra clave 
                nombres.append(element[column2])
                votos.append(float(element[column3]))
                counter += 1
        promedio = sum(votos)/len(votos)
        t1_stop = process_time()
        tiempo = t1_stop-t1_start
        return (nombres,counter,promedio,tiempo)

def req6        

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    
    return 0

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    listaD = lt.newList()   # se require usar lista definida
    listaC = lt.newList() 
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                datos = loadCSVFile("Data\AllMoviesDetailsCleaned.csv","Data\AllMoviesCastingRaw.csv") #llamar funcion cargar datos
                listaD = datos[0]
                listaC = datos[1]
                print("Datos de detalles cargados, ",listaD['size']," elementos cargados")
                print("Datos de casting cargados, ",listaC['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if listaD==None or listaD['size']==0: #obtener la longitud de la lista
                    print("La lista 1 está vacía")
                elif listaC==None or listaC['size']==0: 
                    print('La lista 2 está vacía')
                else: 
                    print("La lista de detalles tiene ",listaD['size']," elementos")
                    print("La lista de casting tiene ",listaC['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if listaD==None or listaD['size']==0: #obtener la longitud de la lista
                    print("La lista de detalles esta vacía")
                elif listaC==None or listaC['size']==0:
                    print("La lista de casting esta vacía")
                else:
                    archivo = input('Ingrese el archivo de búsqueda (Detalles o Casting)\n')   
                    column = input('Ingrese columna de búsqueda\n')
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    if archivo.lower() == 'detalles':
                        counter=countElementsFilteredByColumn(criteria, column, listaD) #filtrar una columna por criterio  
                    elif archivo.lower() == 'casting':
                        counter=countElementsFilteredByColumn(criteria, column, listaC)
                    print("Coinciden ",counter," elementos con el criterio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el criterio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                director = input('Ingrese el nombre del director:\n')
                pelis = req1(listaC, listaD, director, 'director_name', 6, 'vote_average')
                print('El director ', director, ' tiene ', pelis, ' películas buenas.')
            elif int(inputs[0])==6: #opcion 6
                gb1 = int(input('Más Votos (1) o Menos Votos (0):\n'))
                n1 = int(input('¿Cuántas películas?\n'))
                gb2 = int(input('Mejor Promedio (1) o Peor Promedio (0):\n'))
                n2 = int(input('¿Cuántas películas?\n'))
                if gb1 == 1:
                    function1 = greaterfunction
                elif gb1 == 0:
                    function1 = lessfunction
                if gb2 == 1:
                    function2 = greaterfunction
                elif gb2 == 0: 
                    function2 = lessfunction
                resultados1 = req2(listaD, function1, 'vote_count', n1)
                resultados2 = req2(listaD, function2, 'vote_average', n2)
                print('Por votos:\n',resultados1 )
                print('Por promedio:\n', resultados2)
            elif int(inputs[0])==7: #opcion 7
                genero = input('Ingrese el género:\n')
                resultado = req5(listaD, genero, 'genres', 'title', 'vote_average' )
                print ('Las películas de ', genero, 'son:\n', resultado[0])
                print ('Hay ', resultado[1], ' películas de ', genero)
                print('El promedio de votación es de ', resultado[2])
                print('El tiempo fue de ', resultado[3], ' segundos')
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()