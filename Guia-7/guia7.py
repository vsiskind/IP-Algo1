import math

# Ejercicio 1:
# 1.1)
def pertenece(seq:list[int], e:int) -> bool:
    res:bool = False
    for i in seq:
        if i == e:
            res = True
    return res

def pertenece2(seq:list[int], e:int) -> bool:
    res:bool = False
    i:int = 0
    while res == False and i < len(seq):
        if seq[i] == e:
            res = True
        i += 1
    return res

# 1.2)
def divide_a_todos(lista:list[int], e:int) -> bool:
    res:bool = True
    i:int = 0
    while res == True and i < len(lista):
        if lista[i] % e != 0:
            res = False
        i += 1
    return res

def divide_a_todos2(lista:list[int], e:int) -> bool:
    i:int = 0
    while i < len(lista) and lista[i] % e == 0:
        i+=1
    return i == len(lista)

# 1.3)
def suma_total(lista:list[int]) -> int:
    suma:int = 0
    for i in lista:
        suma += i
    return suma

# 1.4)
def maximo(s:list[int]) -> int:
    max:int = s[0]
    for i in s:
        if i > max:
            max = i
    return max

# 1.5)
def minimo(s:list[int]) -> int:
    min:int = s[0]
    for i in s:
        if i < min:
            min = i
    return min

# 1.6)
def ordenados(seq:list[int]) -> bool:
    i:int = 0
    while i+1 < len(seq) and seq[i] < seq[i+1]:
        i += 1
    return i == len(seq) 

# 1.7)
def pos_maximo(seq:list[int]) -> int:
    max = seq[0]
    index_max = 0
    for i in range(len(seq)):
        if seq[i] > max:
            max = seq[i]
            index_max = i
    return index_max

# 1.8)
def pos_minimo(seq:list[int]) -> int:
    max = seq[0]
    index_max = 0
    for i in range(len(seq)):
        if seq[i] < max:
            max = seq[i]
            index_max = i
    return index_max

# 1.9)
def long_mayorASiete(s:list[str]) -> bool:
    i:int = 0
    res:bool = False
    while i < len(s) and not(res):
        if len(s[i]) > 7:
            res = True
        i += 1
    return res

# 1.10)
def es_palindromo(s):
    medio = len(s) / 2
    res = True
    i = 0
    j = len(s) - 1
    while i < medio and res:
        if s[i] != s[j]:
            res = False
        i += 1
        j -= 1
    return res

# 1.11)
def iguales_consecutivos(seq:list[int]) -> bool:
    i:int = 0
    j:int = 1
    k:int = 2
    res:bool = False
    while k < len(seq) and not(res):
        if seq[i] == seq[j] == seq[k]:
            res = True
        i += 1
        j += 1
        k += 1
    return res

# 1.12)
def vocales_distintas(string: str) -> bool:
    lista_vocales:list[str] = ['a', 'e', 'i', 'o', 'u']
    vocales_distintas:list[str] = []
    i:int = 0
    while i < len(string) and len(vocales_distintas) < 3:
        if string[i] in lista_vocales and not(string[i] in vocales_distintas):
            vocales_distintas.append(string[i])
        i += 1
    return len (vocales_distintas) == 3

# 1.13)
def pos_secuencia_ordenada_mas_larga(seq:list[int]) -> int:
    start_index:int = 0
    max_length:int = 0
    i:int = 0
    while i < len(seq):
        j:int = 0
        sorted_length:int = 0
        while i+j < len(seq) - 1 and seq[i+j] <= seq[i+j+1]:
            sorted_length += 1
            j += 1
        if sorted_length > max_length:
            max_length = sorted_length
            start_index = i
        i += 1
    return start_index

# 1.14)
def cantidad_digitos_impares(seq:list[int]) -> int:
    impar_counter:int = 0
    for i in seq:
        while i > 0:
            digito:int = i % 10
            if digito % 2 != 0:
                impar_counter += 1
            i = i // 10
    return impar_counter


# Ejercicio 2:
# 2.1)
def CerosEnPosicionesPares(seq:list[int]):
    for i in range(0, len(seq), 2):
        seq[i] = 0

# 2.2)
def CerosEnPosicionesPares2(seq:list[int]) -> list[int]:
    lista_final = seq
    for i in range (len(seq)):
        if i % 2 == 0:
            lista_final[i] = 0
    return lista_final

lista = ['termo', 'gatoturo', 'tener', 'jirafas']
print(long_mayorASiete(lista))





def promedio(lista:list[int]) -> float:
    counter_lista = 0
    for i in range(len(lista)):
        counter_lista += lista[i]
    return counter_lista / len(lista)