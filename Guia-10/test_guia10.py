import unittest
import guia10
from queue import LifoQueue as Pila
from queue import Queue as Cola

class test_veterinaria(unittest.TestCase):
    def test_stock_productos(self):
        stock_cambios:list[tuple[str, int]] = [
            ('hueso', 10), ('kibble', 20), ('hueso', 15), ('perro', 5), ('kibble', 4)]
        res_dict:dict[str, tuple[int, int]] = {'hueso': (10, 15), 'kibble': (4, 20), 'perro': (5,5)}
        self.assertDictEqual(guia10.stock_productos(stock_cambios), res_dict)

    def test_es_primo(self):
        self.assertTrue(guia10.es_primo(2))
        self.assertTrue(guia10.es_primo(3))
        self.assertTrue(guia10.es_primo(5))
        self.assertFalse(guia10.es_primo(9))
        self.assertFalse(guia10.es_primo(57))
        self.assertTrue(guia10.es_primo(101))
        self.assertTrue(guia10.es_primo(103))
        self.assertTrue(guia10.es_primo(107))

    def test_filtrar_codigos_primos(self):
        lista_codigos:list[int] = [2049339, 2030101, 404019, 1021, 392103, 1003]
        res_lista:list[int] = [2030101, 404019, 392103, 1003]
        self.assertListEqual(res_lista, guia10.filtrar_codigos_primos(lista_codigos))

    def test_subsecuencia_mas_larga(self):
        lista_animales:list[str] = [
            'perro', 'gato', 'loro', 'gato', 'serpiente', 'perro', 'perro', 'gato', 'perro', 'loro']
        self.assertEqual(guia10.subsecuencia_mas_larga(lista_animales), 5)

    def test_primer_subsecuencia_mas_larga(self):
        lista_animales:list[str] = [
            'perro', 'gato', 'loro', 'gato', 'perro', 'perro', 'gato', 'serpiente', 'perro', 'perro', 'gato', 'perro', 'loro']
        self.assertEqual(guia10.subsecuencia_mas_larga(lista_animales), 3)

    def test_un_responsable_por_turno(self):
        grilla_horaria:list[list[str]] = [
            ['valu', 'mariano', 'valu', 'bruni', 'bruni', 'valu', 'analia'],
            ['valu', 'mariano', 'valu', 'bruni', 'bruni', 'valu', 'mariano'],
            ['valu', 'mariano', 'valu', 'bruni', 'bruni', 'valu', 'bruni'],
            ['valu', 'bruni', 'valu', 'analia', 'bruni', 'valu', 'valu'],
            ['bruni', 'bruni', 'analia', 'analia', 'bruni', 'mariano', 'analia'],
            ['bruni', 'bruni', 'analia', 'analia', 'bruni', 'mariano', 'mariano'],
            ['bruni', 'bruni', 'mariano', 'valu', 'bruni', 'mariano', 'bruni'],
            ['bruni', 'bruni', 'mariano', 'valu', 'bruni', 'mariano', 'valu']
        ]
        turnos_eficientes:list[tuple[bool, bool]] = guia10.un_responsable_por_turno(grilla_horaria)
        lista_res:list[tuple[bool, bool]] = [
            (True, True), (False, True), (True, False), (False, False), (True, True), (True, True), (False, False)]
        self.assertEqual(len(turnos_eficientes), 7)
        for i in range(len(lista_res)):
            self.assertEqual(turnos_eficientes[i], lista_res[i])


class test_sala_de_escape(unittest.TestCase):
    def test_promedio_de_salidas(self):
        registro:dict[str, list[int]] = {'Valu': [0, 34, 25, 40, 61], 'Jacob': [48, 21, 0, 61], 'Isa': [32, 0, 61, 29, 0]}
        res_dict:dict[str, tuple[int, float]] = {'Valu': (3, 33.0), 'Jacob': (2, 34.5), 'Isa': (2, 30.5)}
        self.assertDictEqual(guia10.promedio_de_salidas(registro), res_dict)

    def test_tiempo_mas_rapido(self):
        tiempos:list[int] = [0, 34, 25, 40, 61, 48, 21, 0, 61, 32, 0, 61, 29, 0]
        self.assertEqual(guia10.tiempo_mas_rapido(tiempos), 6)


class test_palindromos(unittest.TestCase):
    def test_es_palindromo(self):
        self.assertTrue(guia10.es_palindromo('kayak'))
        self.assertTrue(guia10.es_palindromo('aaaa'))
        self.assertTrue(guia10.es_palindromo('racecar'))
        self.assertTrue(guia10.es_palindromo('hola o aloh'))
        self.assertFalse(guia10.es_palindromo('hola'))
        self.assertFalse(guia10.es_palindromo('notpali'))

    def test_cuantos_sufijos_son_palindromos(self):
        texto:str = 'Diego'
        self.assertEqual(guia10.cuantos_sufijos_son_palindromos(texto), 1)
        texto1:str = 'kayak'
        self.assertEqual(guia10.cuantos_sufijos_son_palindromos(texto1), 2)
        texto2:str = 'ayaya'
        self.assertEqual(guia10.cuantos_sufijos_son_palindromos(texto2), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)