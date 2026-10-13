import math 

# Ejercicio 1:
# 1.1)
def imprimir_hola_mundo ():
    print("hello world")
    
# 1.2)
def imprimir_un_verso ():
    print ("I would go out tonight \nbut I haven't got a stitch to wear")

# 1.3)
def raizDe2 ():
    return round(math.sqrt(2), 4)

# 1.4)
def factorial_de_dos():
    return 2

# 1.5)
def perimetro ():
    return 2 * math.pi


# Ejercicio 2:
# 2.1)
def imprimir_saludo (nombre:str):
    print("Hola " + nombre + "!")

# 2.2)
def raiz_cuadrada_de(numero:int) -> float:
    return math.sqrt(numero)

# 2.3)
def fahrenheit_a_celsius (fahrenheit : int) -> float:
    celsius = ((fahrenheit -32) * 5) / 9
    return celsius

# 2.4)
def imprimir_dos_veces (estribillo : str) -> str:
    print (estribillo * 2)

# 2.5) 
def es_multiplo_de(n:int, m:int) -> bool:
    return (n % m) == 0

# 2.6)
def es_par (numero: int) -> bool:
    return es_multiplo_de(numero, 2)

# 2.7)
def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int:
    total_porciones = comensales * min_cant_de_porciones
    return math.ceil(total_porciones / 8) 


# Ejercicio 3:
# 3.1)
def alguno_es_0(numero1:int, numero2:int) -> bool:
    return numero1 == 0 or numero2 == 0

# 3.2)
def ambos_son_0(numero1:int, numero2:int) -> bool:
    return numero1 == 0 and numero2 ==0

# 3.3)
def es_nombre_largo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

# 3.4)
def es_bisiesto(anio:int) -> bool:
    res:bool = anio % 400 == 0 or (anio % 4 == 0) and (anio % 100 != 0)
    return res


# Ejercicio 4: 
# 4.1)
def peso_pino (altura:float) -> int:
    peso:int = 0
    altura_en_cm:int = int(altura * 100)
    if altura_en_cm <= 300:
        peso = 3 * altura_en_cm
    else:
        peso = 900 + 2 * (altura_en_cm - 300)
    return peso

# 4.2)
def es_peso_util(peso:int) -> bool:
    return peso >= 400 and peso <= 1000

# 4.3)
def sirve_pino(altura:float) -> bool:
    return es_peso_util(peso_pino(altura))


# Ejercicio 5:
# 5.1)
def doble_si_es_par(n:int) -> int:
    resultado:int = n
    if es_par(n):
        resultado *= 2
    return resultado

# 5.2)
def devolver_valor_si_es_par_si_no_el_que_sigue(numero:int) -> int:
    resultado:int = numero
    if not(es_par(numero)):
        resultado += 1
    return resultado

# 5.3)
def doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    res:int = numero
    if numero % 9 == 0:
        res *= 3
    elif numero % 3 == 0:
        res *= 2
    return res

# 5.4)
def lindo_nombre(nombre:str) -> str:
    res:str = ""
    if len(nombre) >= 5:
        res = "Tu nombre tiene muchas letras!"
    else:
        res = "Tu nombre tiene menos de 5 caracteres"
    return res

# 5.5)
def elRango(numero:int):
    if numero < 5:
        print('Menor a 5')
    elif 10 <= numero <= 20:
        print('Entre 10 y 20')
    else:
        print('Mayor a 20')

# 5.6)
def verano(sexo:str, edad:int):
    if sexo == 'M' and (edad < 18 or edad > 65):
        print('anda de vacaciones')
    elif sexo == 'F' and (edad < 18 or edad > 60):
        print('anda de vacaciones')
    else:
        print('Te toca trabajar')


# Ejercicio 6:
# 6.1)
def imprimir_del_1_al_10():
    for i in range(1, 11):
        print(i)

# 6.2)
def imprimir_pares_10_40():
    for i in range (10, 41, 2):
        print(i)

# 6.3)
def imprimir_eco():
    for i in range(10):
        print('eco')

# 6.4)
def cohete(count:int):
    for i in range(count , 0, -1):
        print(i)
    print('Despegue!')

# 6.5)
def time_travel(partida:int, llegada:int):
    while partida > llegada:
        partida -= 1
        print('Viajo un año al pasado, estamos en el año ' + str(partida))

# 6.6)
def time_travel_aristoteles(partida:int):
    while partida > 394:
        partida -= 20
        print('Viajo veinte años al pasado, estamos en el año ' + str(partida))


# Ejercicio 7:
def time_travel_aristoteles2(partida:int):
    for i in range (partida, 384, -20):
        print('Viajo veinte años al pasado, estamos en el año ' + str(i))


# Bonus:
def es_primo (n:int) -> bool:
    es_primo:bool = True
    if n == 1:
        es_primo = False
    else:
        for i in range (2, n-1):
            if n % i == 0:
                es_primo = False
    return es_primo

def cantidad_primos_en_rango (n:int, m:int) -> int:
    counter:int = 0
    while n <= m:
        if es_primo(n):
            counter += 1
        n += 1
    return counter
