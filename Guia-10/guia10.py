import math
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

# Ejercicio 1:
def stock_productos(stock_cambios:list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    res_dict:dict[str, tuple[int, int]] = {}
    for entrada in stock_cambios:
        producto:str = entrada[0]
        cantidad:int = entrada[1]
        if producto not in res_dict:
            res_dict[producto] = (cantidad, cantidad)
        else:
            if cantidad > res_dict[producto][1]:
                res_dict[producto] = (res_dict[producto][1], cantidad)
            else:
                res_dict[producto] = (cantidad, res_dict[producto][1])
    return res_dict


# Ejercicio 2:
def filtrar_codigos_primos(codigos_barra:list[int]) -> list[int]:
    res_lista:list[int] = []
    for codigo in codigos_barra:
        ultimos_tres_digitos:int = codigo % 1000
        if es_primo(ultimos_tres_digitos):
            res_lista.append(codigo)
    return res_lista

def es_primo(num:int) -> bool:
    esPrimo:bool = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            esPrimo = False
    return esPrimo


# Ejercicio 3:
def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str]) -> int:
    indice:int = 0
    max_len:int = 0
    pg_list:list[str] = ['perro', 'gato']
    for i in range(len(tipos_pacientes_atendidos)):
        j:int = i
        temp_len:int = 0
        while j < len(tipos_pacientes_atendidos) and tipos_pacientes_atendidos[j] in pg_list:
            temp_len += 1
            j += 1
        if temp_len > max_len:
            max_len = temp_len
            indice = i
    return indice


# Ejercicio 4:
def un_responsable_por_turno(grilla_horaria:list[list[str]]) -> list[tuple[bool, bool]]:
    res_list:list[tuple[bool, bool]] = []
    for dia in range(7):
        manana_igual:bool = True
        tarde_igual:bool = True
        i:int = 0
        j:int = 4
        responsable_turno_manana = grilla_horaria[0][dia]
        responsable_turno_tarde = grilla_horaria[4][dia]
        while i < 4 and manana_igual:
            if grilla_horaria[i][dia] != responsable_turno_manana:
                manana_igual = False
            i += 1

        while j < 8 and tarde_igual:
            if grilla_horaria[j][dia] != responsable_turno_tarde:
                tarde_igual = False
            j += 1
        res_list.append((manana_igual, tarde_igual))
    return res_list


# Ejercicio 5:
def promedio_de_salidas(registro:dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    promedio_dict:dict[str, tuple[int, float]] = {}
    for key in registro.keys():
        suma_tiempo:int = 0
        salas_logradas:int = 0
        for i in registro[key]:
            if i != 0 and i != 61:
                suma_tiempo += i
                salas_logradas += 1
        promedio_tiempo:float = suma_tiempo / salas_logradas
        promedio_dict[key] = (salas_logradas, promedio_tiempo)
    return promedio_dict


# Ejercicio 6:
def tiempo_mas_rapido(tiempos_salas:list[int]) -> int:
    min:int = 61
    indice:int = 0
    for i in range(len(tiempos_salas)):
        tiempo:int = tiempos_salas[i]
        if 0 < tiempo < 61 and tiempo < min:
            min = tiempo
            indice = i
    return indice


# Ejercicio 11:
def cuantos_sufijos_son_palindromos(texto:str) -> int:
    p_counter:int = 0
    for i in range(len(texto)):
        j:int = i
        sufijo:str = ''
        while j < len(texto):
            sufijo += texto[j]
            j += 1
        if es_palindromo(sufijo):
            p_counter += 1
    return p_counter
    

def es_palindromo(texto:str) -> bool:
    esPalindromo:bool = True
    for i in range(int(len(texto) / 2)):
        if texto[i] != texto[len(texto) - 1 - i]:
            esPalindromo = False
    return esPalindromo