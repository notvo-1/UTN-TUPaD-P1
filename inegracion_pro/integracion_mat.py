from time import time
from sys import setrecursionlimit
from random import randint
import pandas as pd
import matplotlib.pyplot as plt

setrecursionlimit(100000)

def suma_recursiva(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_recursiva(lista[1:])

def suma_loop(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def tm(funcion, lista):
    start = time()
    funcion(lista)
    end = time()
    return (end - start)

def create_list(n, min=0, max=0):
    return [randint(min,max) for _ in range(n)]

####crear listas ####

lista = {
    "list_1" :  create_list(10),
    "list_2" : create_list(100),
    "list_3" : create_list(200),
    "list_4" : create_list(400),
    "list_5" : create_list(800),
    "list_6" : create_list(1600),
    "list_7" : create_list(3200),
    "list_8" : create_list(6400),
}

resultados = []

#### Ejecutar loop de las listas y crear un df ####

for nombre, item in lista.items():
    tiempo_loop = tm(suma_loop, item)
    tiempo_recursiva = tm(suma_recursiva, item)
    resultados.append({
        "Lista": nombre,
        "Recursiva": tiempo_recursiva,
        "Loop": tiempo_loop
    })
print(resultados)    
df = pd.DataFrame(resultados)

#### Graficar ####

df.set_index('Lista')[['Recursiva', 'Loop']].plot(
    marker='o',
    title='Comparación de tiempos de suma',
    ylabel='Tiempo',
    xlabel='Tamaño de la lista',
    grid=True
)
# df.set_index('Lista')[['Loop']].plot(
#     marker='o',
#     title='Comparación de tiempos de suma',
#     ylabel='Tiempo',
#     xlabel='Tamaño de la lista',
#     grid=True
# )
print(df)
plt.show()









