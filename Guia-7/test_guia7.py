import unittest
import guia7

# class test_promedio(unittest.TestCase):
#     def test_promedio_todo_cero(self):
#         self.assertEqual(guia7.promedio([0,0,0,0,0]), 0.0)

#     def test_promedio_todo_1(self):
#             self.assertEqual(guia7.promedio([1,1,1,1,1]), 1.0)

#     def test_promedio_del_uno_al_diez(self):
#             self.assertEqual(guia7.promedio([1,2,3,4,5,6,7,8,9,10]), 5.5)

# class test_pos_secuencia_ordenada_mas_larga(unittest.TestCase):
#     def test_lista_len1(self):
#         self.assertEqual(guia7.pos_secuencia_ordenada_mas_larga([1]), 0)

#     def test_lista_dos_seq_mismo_orden(self):
#         self.assertEqual(guia7.pos_secuencia_ordenada_mas_larga([1,2,4,2,3,4,2,8]), 0)

#     def test_lista_mas_larga_en_el_medio(self):
#             self.assertEqual(guia7.pos_secuencia_ordenada_mas_larga([10,2,4,2,3,4,2,8]), 3)

#     def test_lista_todos_desordenados(self):
#             self.assertEqual(guia7.pos_secuencia_ordenada_mas_larga([5,4,3,2,1]), 0)

class test_cantidad_digitos_impares(unittest.TestCase):
    def test_ejemplo_guia(self):
        self.assertEqual(guia7.cantidad_digitos_impares( [57,2383,812,246]), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)