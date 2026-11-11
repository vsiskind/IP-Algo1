import math
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import TypeVar

T = TypeVar('T')

# Funciones Auxiliares:
def lista_reversa(lista:list) -> list:
    reversa:list = []
    for i in range(len(lista) -1, -1, -1):
        reversa.append(lista[i])
    return reversa

def pila_desde_lista(lista:list[T]) -> Pila[T]:
    pila:Pila[T] = Pila()
    for i in lista:
        pila.put(i)
    return pila

def cola_desde_lista(lista:list[T]) -> Cola[T]:
    cola:Cola[T] = Cola()
    for i in lista:
        cola.put(i)
    return cola

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
    for i in copy_lista:
        cola.put(i)
        copy_cola.put(i)
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


# Ejercicio 5:
def esta_bien_balanceada(s:str) -> bool:
    pila:Pila = Pila()
    res:bool = True
    open_counter:int = 0
    closed_counter:int = 0
    cant_sin_pareja:int = 0
    for i in s:
        if i == '(': 
            pila.put(i)
            open_counter += 1
        elif i == ')':
            pila.put(i)
            closed_counter += 1
    while not pila.empty():
        elem:str = pila.get()
        if elem == '(':
            cant_sin_pareja += 1
        elif elem == ')':
            cant_sin_pareja -= 1
        if pila.empty() and elem == ')':
            res = False

    if open_counter != closed_counter:
        res = False
    elif cant_sin_pareja != 0:
        res = False
    
    return res


# Ejercicio 6:
def evaluar_expresion(exp:str) -> float:
    lista_operadores:list[str] = ['+', '-', '*', '/']
    pila:Pila = Pila()
    for i in range(0, len(exp), 2):
        if exp[i] not in lista_operadores:
            pila.put(exp[i])
        else:
            op2 = int(pila.get())
            op1 = int(pila.get())
            if exp[i] == '+':
                res_op:float = op1 + op2
                pila.put(res_op)
            elif exp[i] == '*':
                res_op:float = op1 * op2
                pila.put(res_op)
            elif exp[i] == '-':
                res_op:float = op1 - op2
                pila.put(res_op)
            elif exp[i] == '/':
                res_op:float = op1 / op2
                pila.put(res_op)
    return pila.get()


# Ejercicio 7
def intercalar(p1:Pila, p2:Pila) -> Pila:
    p1_copy:Pila = copiar_pila(p1)
    p2_copy:Pila = copiar_pila(p2)
    lista_intercalada_reversa:list = []
    while not p1_copy.empty() and not p2_copy.empty():
        elem2 = p2_copy.get()
        elem1 = p1_copy.get()
        lista_intercalada_reversa.append(elem2)
        lista_intercalada_reversa.append(elem1)
    lista_intercalada:list = lista_reversa(lista_intercalada_reversa)
    return pila_desde_lista(lista_intercalada)


# Ejercicio 8:
def generar_nros_al_azar_cola(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    cola:Cola[int] = Cola()
    for i in range(cantidad):
        cola.put(random.randint(desde, hasta))
    return cola


# Ejercicio 9:
def cantidad_elementos_cola(cola:Cola) -> int:
    lista:list = []
    cola_copy:Cola = copiar_cola(cola)
    while not cola_copy.empty():
        lista.append(cola_copy.get())
    return len(lista)


# Ejercicio 10:
def buscar_el_maximo_cola(cola:Cola[int]):
    cola_copy:Cola[int] = copiar_cola(cola)
    max:int = cola_copy.get()
    while not cola_copy.empty():
        elem = cola_copy.get()
        if elem > max:
            max = elem
    return max


# Ejercicio 11:
def buscar_nota_minima_cola(cola:Cola[tuple[str, int]]) -> tuple[str, int]:
    lista_notas:list[tuple[str, int]] = []
    copy_cola = copiar_cola(cola)
    while not copy_cola.empty():
        lista_notas.append(copy_cola.get())
    min:int = lista_notas[0][1]
    min_tuple:tuple[str, int] = lista_notas[0]
    for elem in lista_notas:
        if elem[1] < min:
            min_tuple = elem
    return min_tuple


# Ejercicio 12:
def intercalar_cola(c1:Cola, c2:Cola) -> Cola:
    c1_copy:Cola = copiar_cola(c1)
    c2_copy:Cola = copiar_cola(c2)
    lista_intercalada:list = []
    while not c1_copy.empty() and not c2_copy.empty():
        lista_intercalada.append(c1_copy.get())
        lista_intercalada.append(c2_copy.get())
    return cola_desde_lista(lista_intercalada)


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


# Ejercicio 14:
def pacientes_urgentes(cola:Cola[tuple[int, str, str]]) -> int:
    cola_copy:Cola = copiar_cola(cola)
    pacientes_urgente:int = 0
    while not cola_copy.empty():
        paciente = cola_copy.get()
        if paciente[0] < 4:
            pacientes_urgente += 1
    return pacientes_urgente


# Ejercicio 15:
def atencion_a_clientes(cola:Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    cola_copy:Cola = copiar_cola(cola)
    lista_clientes:list = []
    cola_ordenada:Cola = Cola()
    while not cola_copy.empty():
        lista_clientes.append(cola_copy.get())

    for i in lista_clientes:
        if i[2] and i[3]:
            cola_ordenada.put(i)
            lista_clientes.remove(i)
    for i in lista_clientes:
        if i[3]:
            cola_ordenada.put(i)
            lista_clientes.remove(i)
    for i in lista_clientes:
        if i[2]:
            cola_ordenada.put(i)
            lista_clientes.remove(i)
    for i in lista_clientes:
        cola_ordenada.put(i)

    return cola_ordenada


# Ejercicio 16:
def calcular_promedio_por_estudiante(notas:list[tuple[str, float]]) -> dict[str, float]:
    cantidad_dict:dict[str, int] = {}
    res_dict:dict[str, float] = {}
    for i in notas:
        nombre:str = i[0]
        if nombre not in cantidad_dict:
            cantidad_dict[nombre] = 1
            res_dict[nombre] = i[1]
        else:
            cantidad_dict[nombre] += 1
            res_dict[nombre] += i[1]
    for nombre in res_dict.keys():
        res_dict[nombre] /= cantidad_dict[nombre]
    return res_dict


# Ejercicio 17:
# 17.1)
historiales:dict[str, Pila[str]]

# 17.2)
def visitar_sitio(historiales:dict[str, Pila[str]], usuario:str, sitio: str) -> None:
    if usuario in historiales:
        historiales[usuario].put(sitio)
    else:
        historial_usuario:Pila[str] = Pila()
        historial_usuario.put(sitio)
        historiales[usuario] = historial_usuario

# 17.3)
def navegar_atras(historiales:dict[str, Pila[str]], usuario:str) -> str:
    sitio_activo:str = historiales[usuario].get()
    return sitio_activo


# Ejercicio 18:
# 18.1)
def agregar_producto(inventario:dict[str, dict[str, float | int]], nombre:str, precio:float, cantidad:int) -> None:
    producto:dict[str, float | int] = {'precio': precio, 'cantidad': cantidad}
    inventario[nombre] = producto

# 18.2)
def actualizar_stock(inventario:dict[str, dict[str, float | int]], nombre:str, cantidad:int) -> None:
    inventario[nombre]['cantidad'] = cantidad

# 18.3)
def actualizar_precio(inventario:dict[str, dict[str, float | int]], nombre:str, precio:float) -> None:
    inventario[nombre]['precio'] = precio

# 18.4)
def calcular_valor_inventario(inventario:dict[str, dict[str, float | int]]) -> float:
    valor_total:float = 0
    for producto in inventario.keys():
        valor_total += inventario[producto]['precio'] * inventario[producto]['cantidad']
    return valor_total


# Ejercicio 19:
# 19.1)
def contar_lineas(nombre_archivo:str) -> int:
    with open(nombre_archivo, 'r') as file:
        lineas:list[str] = file.readlines()
    return len(lineas)

# 19.2)
def existe_palabra(nombre_archivo:str, palabra:str) -> bool:
    contiene_palabra:bool = False
    with open(nombre_archivo, 'r') as file:
        for linea in file:
            if palabra in linea:
                contiene_palabra = True
    return contiene_palabra

# 19.3)
def cantidad_de_apariciones(nombre_archivo:str, palabra:str) -> int:
    cant_de_apariciones:int = 0
    with open(nombre_archivo, 'r') as file:
        for linea in file:
            print(linea)
            if palabra in linea:
                cant_de_apariciones += cant_de_apariciones_por_linea(linea, palabra)
    return cant_de_apariciones

def cant_de_apariciones_por_linea(linea:str, palabra:str) -> int:
    counter:int = 0
    palabras_en_linea:list[str] = separar_string_en_palabras(linea)
    for i in palabras_en_linea:
        if i == palabra:
            counter += 1 
    return counter

def separar_string_en_palabras(linea:str) -> list[str]:
    lista_separadores:list[str] = [' ', '.', ',', ';', ':', '\"', '\'', '¡', '!', '¿', '?', '(', ')', '[', ']', '{', '}', '<', '>', '\n']
    lista_palabras:list[str] = []
    temp_palabra:str = ''
    for i in linea:
        if i not in lista_separadores:
            temp_palabra += i
        else:
            lista_palabras.append(temp_palabra)
            temp_palabra = ''
    if temp_palabra != '':
        lista_palabras.append(temp_palabra)

    return lista_palabras
