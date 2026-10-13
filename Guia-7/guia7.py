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
    return i == len(seq)-1

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

# 2.3)
def sin_vocales(s:str) -> str:
    lista_vocales:list[str] = ['a', 'e', 'i', 'o', 'u']
    res:str = ''
    for letra in s:
        if not(letra in lista_vocales):
            res += letra
    return res

# 2.4)
def reemplaza_vocales(s:str) -> str:
    lista_vocales:list[str] = ['a', 'e', 'i', 'o', 'u']
    res:str = ''
    for letra in s:
        if letra in lista_vocales:
            res += '-'
        else:
            res += letra
    return res

# 2.5)
def da_vuelta_str(s:str) -> str:
    res:str = ''
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

# 2.6)
def eliminar_repetidos(s:str) -> str:
    res:str = ''
    for i in s:
        if not(i in res):
            res += i
    return res


# Ejercicio 3:
def resultadoMateria(notas:list[int]) -> int:
    res:int = 0
    avg:float = promedio(notas)
    i:int = 0
    aprobado:bool = True
    while i < len(notas) and aprobado:
        if notas[i] < 4:
            aprobado = False
        i += 1
    if aprobado and avg >= 7:
        res = 1
    elif aprobado and avg >= 4:
        res = 2
    else:
        res = 3
    return res

def promedio(lista:list[int]) -> float:
    return suma_total(lista) / len(lista)


# Ejercicio 4:
def saldoActual(movimientos:list[tuple]) -> int:
    saldo = 0
    for tup in movimientos:
        if tup[0] == 'I':
            saldo += tup[1]
        elif tup[0] == 'R':
            saldo -= tup[1]
    return saldo


# Ejercicio 5:
# 5.2)
def pertenece_a_cada_uno_v2(matriz:list[list[int]], e:int, res:list[bool]):
    for lista in matriz:
        if pertenece2(lista, e):
            res.append(True)
        else:
            res.append(False)
    return res

# 5.3)
def pertenece_a_cada_uno_v3(matriz:list[list[int]], e:int) -> list[bool]:
    res:list[bool] = []
    for lista in matriz:
        if pertenece2(lista, e):
            res.append(True)
        else:
            res.append(False)
    return res


# Ejercicio 6:
# 6.1)
def es_matriz(s:list[list[int]]) -> bool:
    i:int = 0
    res = True
    if len(s) == 0:
        res = False
    while i < len(s)-1 and res:
        if len(s[i]) == 0 or len(s[i]) != len(s[0]):
            res = False
        i += 1
    return res

# 6.2)
def filas_ordenadas(matriz:list[list[int]], res:list[bool]):
    for i in matriz:
        res.append(ordenados(i))
    return res

# 6.3)
def columna(matriz:list[list[int]], c:int) -> list[int]:
    res:list[int] = []
    for i in matriz:
        res.append(i[c])
    return res

# 6.4)
def columnas_ordenadas(matriz:list[list[int]]) -> list[bool]:
    res:list[bool] = []
    for i in range(len(matriz[0])):
        res.append(ordenados(columna(matriz, i)))
    return res

# 6.5)
def transponer(matriz:list[list[int]]) -> list[list[int]]:
    res:list[list[int]] = []
    for i in range(len(matriz[0])):
        res.append(columna(matriz, i))
    return res

# 6.6)
def quien_gana_tateti(matriz:list[str]) -> int:
    res:int = 2
    horizontal:int = chequeo_horizontal(matriz)
    vertical:int = chequeo_vertical(matriz)
    diagonal:int = chequeo_diagonal(matriz)
    if (horizontal + vertical + diagonal) == 4:
        res = 0
    elif (horizontal + vertical + diagonal) == 5:
        res = 1
    return res

def chequeo_horizontal(matriz:list[str]) -> int:
    res:int = 2
    for i in matriz:
        if i == 'OOO':
            res = 0
        elif i == 'XXX':
            res = 1
    return res

def chequeo_vertical(matriz:list[str]) -> int:
    res:int = 2
    for i in range(3):
        if columna_str(matriz, i) == 'OOO':
            res = 0
        elif columna_str(matriz, i) == 'XXX':
            res = 1
    return res

def chequeo_diagonal(matriz:list[str]) -> int:
    res:int = 2
    diagonal1:str = ''
    diagonal2:str = ''
    for i in range(3):
        diagonal1 += matriz[i][i]
        diagonal2 += matriz[2-i][i]
    if diagonal1 == 'OOO' or diagonal2 == 'OOO':
        res = 0
    elif diagonal1 == 'XXX' or diagonal2 == 'XXX':
        res = 1
    return res

def columna_str(matriz:list[str], c:int) -> str:
    res:str = ''
    for i in matriz:
        res += i[c]
    return res

# Ejercicio 7:

    
tateti = ['OOO',
          'OXX',
          'XXO']
print(quien_gana_tateti(tateti))
