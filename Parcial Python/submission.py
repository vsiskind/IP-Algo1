from queue import LifoQueue as Pila

# Ejercicio 1

def ejercicio1(s: list[int], objetivo: int) -> tuple[int, int]:
	res:tuple[int, int] = (0, 1)
	diferencia:int = len(s)
	for i in range(len(s)):
		j = i + 1
		while j < len(s):
			if s[i] + s[j] == objetivo:
				if j-i <= diferencia:
					res = (i ,j)
					diferencia = j-i
			j += 1
	return res


# Ejercicio 4

def separar_pedidos_express(pedidos: Pila[tuple[int, bool]]) -> Pila[int]:
	lista_pedidos:list[tuple[int, bool]] = []
	pedidos_express:Pila[int] = Pila()

	while not pedidos.empty():
		lista_pedidos.append(pedidos.get())

	for i in range(len(lista_pedidos) -1, -1, -1):
		pedido:tuple[int, bool] = lista_pedidos[i]
		if pedido[1] == True:
			pedidos_express.put(pedido[0])
		else:
			pedidos.put(pedido)

	return pedidos_express


# Ejercicio 5

def ejercicio5(A: list[list[int]]) -> None:
	ubicacion_max:tuple[int, int] = encontrar_ubicacion_maximo(A)
	fila_max = ubicacion_max[0]
	col_max = ubicacion_max[1]
	for i in range(len(A[fila_max])):
		A[fila_max][i] *= 2

def encontrar_ubicacion_maximo(matriz: list[list[int]]) -> tuple[int, int]:
	max:int = matriz[0][0]
	ubicacion_max:tuple[int, int] = (0,0)
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if matriz[i][j] > max:
				max = matriz[i][j]
				ubicacion_max = (i, j)
	return ubicacion_max


# Ejercicio 7

def estudiantes_destacados_por_cantidad_de_cursos(calificaciones: dict[str, list[int]], nota_minima: int) -> dict[int, list[str]]:
	cant_cursos_dict:dict[int, list[str]] = {}
	for estudiante in calificaciones.keys():
		notas:list[int] = calificaciones[estudiante]
		if es_estudiante_destacado(notas, nota_minima):
			if len(notas) not in cant_cursos_dict.keys():
				cant_cursos_dict[len(notas)] = [estudiante]
			else:
				cant_cursos_dict[len(notas)].append(estudiante)
	return cant_cursos_dict

def es_estudiante_destacado(lista_notas:list[int], nota_minima:int) -> bool:
	estudiante_destacado:bool = True
	for i in lista_notas:
		if i < nota_minima:
			estudiante_destacado = False
	return estudiante_destacado

# Entrega Valentin Siskind 15:40