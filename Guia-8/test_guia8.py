import unittest
import guia8
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import TypeVar

class test_esta_bien_balanceada(unittest.TestCase):
    def test_bien_balanceada(self):
        self.assertTrue(guia8.esta_bien_balanceada("1 + (2 x 3 - (20 / 5))"))
        self.assertTrue(guia8.esta_bien_balanceada("10 * (1 + (2 * (-1)))"))
    def test_mal_balanceada(self):
        self.assertFalse(guia8.esta_bien_balanceada("1 + ) 2 x 3 ( ()"))
        self.assertFalse(guia8.esta_bien_balanceada("1 + ( 2 x ( 4 )"))

class test_evaluar_expresion(unittest.TestCase):
    def test_evaluada_bien(self):
        self.assertAlmostEqual(guia8.evaluar_expresion('3 4 + 5 * 2 -'), 33)
        self.assertAlmostEqual(guia8.evaluar_expresion('3 4 + 5 * 2 - 2 /'), 16.5)

class test_intercalar(unittest.TestCase):
    def test_bien_intercalada(self):
        pila1 = Pila()
        for i in range(1, 11, 2):
            pila1.put(i)
        pila2 = Pila()
        for i in range(0, 11, 2):
            pila2.put(i)
        pilaRes = Pila()
        for i in range(11):
            pilaRes.put(i)
        pilaTest = guia8.intercalar(pila1, pila2)
        while not pilaTest.empty() and not pilaRes.empty():
            self.assertEqual(pilaTest.get(), pilaRes.get())

class test_generar_nros_al_azar_cola(unittest.TestCase):
    def test_cola_es_largo_cantidad(self):
        cola:Cola = guia8.generar_nros_al_azar_cola(10, 1, 10)
        self.assertEqual(guia8.cantidad_elementos_cola(cola), 10)

class test_buscar_el_maximo_cola(unittest.TestCase):
    def test_maximo_ok(self):    
        lista = [1,5,8,2,7,0,3,5,4]
        cola = guia8.cola_desde_lista(lista)
        self.assertEqual(guia8.buscar_el_maximo_cola(cola), 8)

class test_buscar_nota_minima_cola(unittest.TestCase):
    def test_minimo_ok(self):
        cola:Cola = Cola()
        cola.put(('M', 5))
        cola.put(('A', 3))
        cola.put(('S', 8))
        cola.put(('V', 10))
        cola.put(('R', 2))
        self.assertEqual(guia8.buscar_nota_minima_cola(cola), ('R', 2))

class test_intercalar_cola(unittest.TestCase):
    def test_bien_intercalada_cola(self):
        l1 = [1,3,5,7,9]
        l2 = [2,4,6,8,10]
        cola1:Cola = guia8.cola_desde_lista(l1)
        cola2:Cola = guia8.cola_desde_lista(l2)
        lres = [1,2,3,4,5,6,7,8,9,10]
        colaRes:Cola = guia8.cola_desde_lista(lres)
        colaTest = guia8.intercalar_cola(cola1, cola2)
        while not colaTest.empty() and not colaRes.empty():
            self.assertEqual(colaTest.get(), colaRes.get())

class test_bingo(unittest.TestCase):
    def test_armar_secuencia_ok(self):
        lista_0_100:list[int] = list(range(100))
        secuencia:Cola[int] = guia8.armar_secuencia_de_bingo()
        while not secuencia.empty():
            num:int = secuencia.get()
            self.assertIn(num, lista_0_100)
            lista_0_100.remove(num)
        self.assertTrue(lista_0_100 == [])

    def test_jugar_carton_de_bingo_ok(self):
        secuencia_carta:Cola[int] = guia8.armar_secuencia_de_bingo()
        carta:list[int] = []
        for i in range(12):
            carta.append(secuencia_carta.get())
        bolillero = guia8.armar_secuencia_de_bingo()
        ronda = guia8.jugar_carton_de_bingo(carta, bolillero)
        self.assertTrue(12 <= ronda <= 100)

    # def test_promedio_juego(self):
    #     suma = 0
    #     for i in range(10000):
    #         secuencia_carta:Cola[int] = guia8.armar_secuencia_de_bingo()
    #         carta:list[int] = []
    #         for i in range(12):
    #             carta.append(secuencia_carta.get())
    #         bolillero = guia8.armar_secuencia_de_bingo()
    #         ronda = guia8.jugar_carton_de_bingo(carta, bolillero)
    #         suma += ronda

    #     promedio = 0
    #     promedio = suma / 10000
    #     self.assertAlmostEqual(promedio, 93.2, 1)

class test_guardia_medica(unittest.TestCase):
    def test_cant_pacientes_urgentes(self):
        lista_pacientes:list[tuple[int, str, str]] = [
            (2, 'valen', 'traumatologia'),
            (5, 'toler', 'otorrinologia'),
            (9, 'pedro', 'laringologia'),
            (1, 'colidio', 'ginecologia'),
            (3, 'george', 'pediatria')
        ]
        cola_pacientes:Cola = guia8.cola_desde_lista(lista_pacientes)
        self.assertTrue(guia8.pacientes_urgentes(cola_pacientes) == 3)


class test_fila_banco(unittest.TestCase):
    def test_orden_de_fila(self):
        lista_clientes:list[tuple[str, int, bool, bool]] = [
            ('valen', 3637304, True, False),
            ('toler', 6947839, False, False),
            ('pedro', 2048958, False, False),
            ('martinez quarta', 4934720, False, True),
            ('jorge brito', 5834028, True, True),
        ]
        cola_clientes:Cola = guia8.cola_desde_lista(lista_clientes)

        lista_clientes_ordenada:list[tuple[str, int, bool, bool]] = [
            ('jorge brito', 5834028, True, True),
            ('martinez quarta', 4934720, False, True),
            ('valen', 3637304, True, False),
            ('toler', 6947839, False, False),
            ('pedro', 2048958, False, False),
        ]
        cola_clientes_ordenada:Cola = guia8.cola_desde_lista(lista_clientes_ordenada)

        cola_test:Cola = guia8.atencion_a_clientes(cola_clientes)
        while not cola_test.empty() and not cola_clientes_ordenada.empty():
            c_test = cola_test.get()
            c_ord = cola_clientes_ordenada.get()
            self.assertEqual(c_test, c_ord)

class test_calcular_promedio_por_estudiante(unittest.TestCase):
    def test_promedio_ok(self):
        notas:list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
        res_dict:dict = {"Sole": 9.25, "Maxi": 8.0}
        self.assertDictEqual(guia8.calcular_promedio_por_estudiante(notas), res_dict)

class test_navegador_de_web(unittest.TestCase):
    def test_visitar_sitio_misma_persona(self):
        v_historial:Pila = Pila()
        v_historial.put('youtube.com')
        v_historial.put('cubawiki.com.ar')
        historiales:dict[str, Pila[str]] = {'Valu': v_historial}
        p_resultado:Pila = Pila()
        p_resultado.put('youtube.com')
        p_resultado.put('cubawiki.com.ar')
        p_resultado.put('campus.exactas.uba.ar')
        guia8.visitar_sitio(historiales, 'Valu', 'campus.exactas.uba.ar')
        for i in historiales.keys():
            pila:Pila = historiales[i]
            while not pila.empty():
                self.assertEqual(pila.get(), p_resultado.get())

    def test_visitar_sitio_persona_distinta(self):
        v_historial:Pila = Pila()
        v_historial.put('youtube.com')
        v_historial.put('cubawiki.com.ar')
        historiales:dict[str, Pila[str]] = {'Valu': v_historial}
        v_resultado:Pila = Pila()
        v_resultado.put('youtube.com')
        v_resultado.put('cubawiki.com.ar')
        b_resultado:Pila = Pila()
        b_resultado.put('netflix.com')
        guia8.visitar_sitio(historiales, 'Bruni', 'netflix.com')
        print(historiales)
        self.assertEqual(historiales['Bruni'].get(), b_resultado.get())
        while not historiales['Valu'].empty():
            self.assertEqual(historiales['Valu'].get(), v_resultado.get())

    def test_navegar_atras(self):
        v_historial:Pila = Pila()
        v_historial.put('youtube.com')
        v_historial.put('cubawiki.com.ar')
        b_historial:Pila = Pila()
        b_historial.put('netflix.com')
        historiales:dict[str, Pila[str]] = {'Valu': v_historial, 'Bruni': b_historial}
        self.assertEqual(guia8.navegar_atras(historiales, 'Valu'), 'cubawiki.com.ar')
        self.assertEqual(historiales['Valu'].get(), 'youtube.com')

class test_tienda_de_ropa(unittest.TestCase):
    def test_calcular_valor_inventario(self):
        inventario = {}
        guia8.agregar_producto(inventario, "Camisa", 20.0, 50)
        guia8.agregar_producto(inventario, "Pantalon", 30.0, 30)
        guia8.actualizar_stock(inventario, "Camisa", 10)
        valor_total = guia8.calcular_valor_inventario(inventario)
        self.assertEqual(valor_total, 1100.0)

class test_archivos_basicos(unittest.TestCase):
    def test_contar_lineas(self):
        nombre_archivo:str = 'Guia-8/archivos/texto.txt'
        self.assertEqual(guia8.contar_lineas(nombre_archivo), 4)

    def test_existe_palabra(self):
        nombre_archivo:str = 'Guia-8/archivos/texto.txt'
        palabra:str = 'River'
        self.assertTrue(guia8.existe_palabra(nombre_archivo, palabra))
        self.assertFalse(guia8.existe_palabra(nombre_archivo, 'Boca'))

    def test_cantidad_de_apariciones(self):
        nombre_archivo:str = 'Guia-8/archivos/texto.txt'
        palabra:str = 'Valu'
        self.assertEqual(guia8.cantidad_de_apariciones(nombre_archivo, palabra), 4)
       
        

if __name__ == '__main__':
    unittest.main(verbosity=2)