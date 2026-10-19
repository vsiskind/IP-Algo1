import math
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import TypeVar

T = TypeVar('T')

# Funciones Auxiliares:
def pila_desde_lista(lista:list[int]) -> Pila[int]:
    pila:Pila[int] = Pila()
    for i in lista:
        pila.put(i)
    return pila

def mostrar_pila(pila:Pila[T]):
    copy_pila:Pila[T] = Pila()
    while not(pila.empty()):
        elem = pila.get()
        copy_pila.put(elem)
        print(elem)
    while not(copy_pila.empty()):
        pila.put(copy_pila.get())

def copiar_pila(pila:Pila[T]) -> Pila[T]:
    copy_lista:list[T] = []
    copy_pila:Pila[T] = Pila()
    while not(pila.empty()):
        elem = pila.get()
        copy_lista.append(elem)
    i:int = len(copy_lista)-1
    while i >= 0:
        pila.put(copy_lista[i])
        copy_pila.put(copy_lista[i])
        i -= 1
    return copy_pila

def mostrar_cola(cola:Cola[T]):
    copy_cola:Cola[T] = Cola()
    while not(cola.empty()):
        elem = cola.get()
        copy_cola.put(elem)
        print(elem)
    while not(copy_cola.empty()):
        cola.put(copy_cola.get())

def copiar_cola(cola:Cola[T]) -> Cola[T]:
    copy_lista:list[T] = []
    copy_cola:Cola[T] = Cola()
    while not(cola.empty()):
        elem = cola.get()
        copy_lista.append(elem)
    i:int = len(copy_lista)-1
    while i >= 0:
        cola.put(copy_lista[i])
        copy_cola.put(copy_lista[i])
        i -= 1
    return copy_cola


# Ejercicio 1:
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    pila:Pila[int] = Pila()
    for i in range(cantidad):
        pila.put(random.randint(desde, hasta))
    return pila

# Ejercicio 2:
def cantidad_elementos(p:Pila[int]) -> int:
    res:int = 0
    temp_pila:Pila[int] = copiar_pila(p)
    while not(temp_pila.empty()):
        temp_pila.get()
        res += 1
    return res

# Ejercicio 3:
def buscar_el_maximo(p:Pila[int]) -> int:
    temp_pila:Pila[int] = copiar_pila(p)
    max:int = temp_pila.get()
    while not(temp_pila.empty()):
        elem:int = temp_pila.get()
        if elem > max:
            max = elem
    return max

# Ejercicio 4:
def buscar_nota_maxima(p:Pila[tuple]) -> int:
    temp_pila:Pila[tuple] = copiar_pila(p)
    max:int = temp_pila.get()[1]
    while not(temp_pila.empty()):
        elem = temp_pila.get()[1]
        if elem > max:
            max = elem
    return max

# Ejercicio 13:
# 13.1)
def armar_secuencia_de_bingo() -> Cola[int]:
    secuencia_bingo:Cola[int] = Cola()
    lista_bola:list[int] = list(range(100))
    random.shuffle(lista_bola)
    for i in lista_bola:
        secuencia_bingo.put(i)
    return secuencia_bingo

# 13.2)
def jugar_carton_de_bingo(carton:list[int], bolillero:Cola[int]) -> int:
    res:int = 0
    carton_copy:list[int] = carton.copy()
    bolillero_copy:Cola[int] = copiar_cola(bolillero)
    while not(bolillero_copy.empty()) and len(carton_copy) > 0:
        num:int = bolillero_copy.get()
        if num in carton_copy:
            carton_copy.remove(num)
        res += 1
    return res


# sum = 0
# for i in range(100):
#     bolacarta = armar_secuencia_de_bingo()
#     carta = []
#     for i in range(12):
#         carta.append(bolacarta.get())
#     bolillero = armar_secuencia_de_bingo()
#     ronda = jugar_carton_de_bingo(carta, bolillero)
#     sum += ronda

# promedio = 0
# promedio = sum / 100
# print(promedio)
    
bolacarta = armar_secuencia_de_bingo()
carta = []
for i in range(12):
    carta.append(bolacarta.get())
bolillero = armar_secuencia_de_bingo()
ronda = jugar_carton_de_bingo(carta, bolillero)

print(carta)
mostrar_cola(bolillero)

# pila = generar_nros_al_azar(5, 0, 10)
# mostrar_pila(pila)
# print('---')
# print(buscar_el_maximo(pila))