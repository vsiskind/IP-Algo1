import unittest
import guia6

class test_fahrenheit_a_celcius(unittest.TestCase):
    def test_agua_hierve(self):
        self.assertEqual(guia6.fahrenheit_a_celsius(212), 100.0)

    def test_agua_congela(self):
        self.assertEqual(guia6.fahrenheit_a_celsius (32), 0.0)

class test_es_primo(unittest.TestCase):
    def test_es_primo_7(self):
        self.assertTrue(guia6.es_primo(7))

    def test_es_primo_9(self):
        self.assertFalse(guia6.es_primo(9))

class test_doble_si_es_par(unittest.TestCase):
    def test_impar(self):
        self.assertEqual(guia6.doble_si_es_par(5), 5)

    def test_par(self):
        self.assertEqual(guia6.doble_si_es_par(4), 8)

class test_es_primo_en_rango(unittest.TestCase):
    def test_rango_1_10(self):
        self.assertEqual(guia6.cantidad_primos_en_rango(1, 10), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)