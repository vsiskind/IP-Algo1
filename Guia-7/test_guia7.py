import unittest
import guia7

class test_promedio(unittest.TestCase):
    def test_promedio_todo_cero(self):
        self.assertEqual(guia7.promedio([0,0,0,0,0]), 0.0)

    def test_promedio_todo_1(self):
            self.assertEqual(guia7.promedio([1,1,1,1,1]), 1.0)

    def test_promedio_del_uno_al_diez(self):
            self.assertEqual(guia7.promedio([1,2,3,4,5,6,7,8,9,10]), 5.5)


if __name__ == '__main__':
    unittest.main(verbosity=2)