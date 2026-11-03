import unittest
from arimaa import *

# Las piezas se representan con las siguientes letras:
#   E : elefante
#   M : camello
#   H : caballo
#   D : perro
#   C : gato
#   R : ratón
# donde
#   mayúscula : dorado
#   minúscula : plateado

def tablero_8x8_vacio():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

def tablero_8x8_inicial_ejemplo():
    return leer_tablero([
              'hcdmedch', #7
              'rrrrrrrr', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              'RRRRRRRR', #1
              'HCDMEDCH', #0
              #01234567
            ])

def tablero_7x8_ejemplo():
    return leer_tablero([
        'hcdmedch', #6
        'rrrrrrrr', #5
        '--------', #4
        '--------', #3
        '--------', #2
        'RRRRRRRR', #1
        'HCDMEDCH', #0
        #01234567
    ])

def tablero_8x7_ejemplo():
    return leer_tablero([
        'hcdmedc', #7
        'rrrrrrr', #6
        '-------', #5
        '-------', #4
        '-------', #3
        '-------', #2
        'RRRRRRR', #1
        'HCDMEDC', #0
        #0123456
    ])

def tablero_7x7_ejemplo():
    return leer_tablero([
        'hcdmedc', #6
        'rrrrrrr', #5
        '-------', #4
        '-------', #3
        '-------', #2
        'RRRRRRR', #1
        'HCDMEDC', #0
        #0123456
    ])

### Ejercicio 1

class test_tablero_bien_formado(unittest.TestCase):

    def test_8x8_lleno(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

    def test_8x8_vacio(self):
        t = tablero_8x8_vacio()
        self.assertTrue(tablero_bien_formado(t))

    def test_7x8(self):
            t = tablero_7x8_ejemplo()
            self.assertFalse(tablero_bien_formado(t))

    def test_8x7(self):
                t = tablero_8x7_ejemplo()
                self.assertFalse(tablero_bien_formado(t))

    def test_7x7(self):
                t = tablero_7x7_ejemplo()
                self.assertFalse(tablero_bien_formado(t))

class test_posicion_en_tablero(unittest.TestCase):

    def test_posicion_ok(self):
        self.assertTrue(posicion_en_tablero(Posicion(5, 3)))
        self.assertTrue(posicion_en_tablero(Posicion(0, 0)))
        self.assertTrue(posicion_en_tablero(Posicion(0, 7)))
        self.assertTrue(posicion_en_tablero(Posicion(7, 0)))
        self.assertTrue(posicion_en_tablero(Posicion(7, 7)))
        self.assertTrue(posicion_en_tablero(Posicion(3, 4)))
    
    def test_posicion_mal(self):
        self.assertFalse(posicion_en_tablero(Posicion(8, 8)))
        self.assertFalse(posicion_en_tablero(Posicion(0, 8)))
        self.assertFalse(posicion_en_tablero(Posicion(8, 0)))
        self.assertFalse(posicion_en_tablero(Posicion(-1, -1)))
        self.assertFalse(posicion_en_tablero(Posicion(10, 6)))
        self.assertFalse(posicion_en_tablero(Posicion(2, 10)))

class test_movimiento_bien_formado(unittest.TestCase):

    def test_movimiento_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])))
        self.assertTrue(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(5,2), [NORTE, SUR])))
        self.assertTrue(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(6,1), [ESTE, ESTE])))

    def test_movimiento_mal(self):
        #si la pieza está fuera del tablero
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 9), [NORTE])))
        #Mover a secas con movimientos de más
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(6,2), [OESTE, SUR])))
        #Arrastrar con movimientos de menos
        self.assertFalse(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(5,3), [SUR])))
        #Arrastrar con movimientos de más
        self.assertFalse(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(5,3), [SUR,NORTE,OESTE])))
        #Empujar con movimientos de menos
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(6,1), [ESTE])))
        #Empujar con movimientos de mas
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(5,2), [NORTE, SUR, ESTE])))


class test_juego_bien_formado(unittest.TestCase):

    def test_juego_ok(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))

    def test_juego_demasiados_pasos(self):
        j = Juego(tablero_8x8_vacio(), PLATEADO, 4)
        self.assertFalse(juego_bien_formado(j))

    def test_juego_tablero_malo(self):
        j = Juego(tablero_7x8_ejemplo(), DORADO, 3)
        self.assertFalse(juego_bien_formado(j))

    def test_juego_tablero_malo_y_demasiados_pasos(self):
        j = Juego(tablero_7x8_ejemplo(), DORADO, 5)
        self.assertFalse(juego_bien_formado(j))

#### Ejercicio 2

class test_posicion_vecina_hacia(unittest.TestCase):

    def test_vecina_al_norte(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))

class test_son_posiciones_vecinas(unittest.TestCase):

    def test_vecinas(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))

class test_casilla_en_posicion(unittest.TestCase):

    def test_casilla_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))
        self.assertEqual(casilla_en_posicion(t, Posicion(4, 4)), VACIA)

class test_hay_casilla_vacia(unittest.TestCase):

    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))

    def test_casilla_ocupada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(1,1)))

class test_hay_pieza_de_color(unittest.TestCase):

    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))
        
    def test_no_hay_pieza_(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(4, 1), PLATEADO))

#### Ejercicio 3

class test_hay_casilla_vacia_hacia(unittest.TestCase):

    def test_hay_casilla_vacia_hacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(0, 0), NORTE))

    def test_hay_casilla_vacia_hacia_fuera_del_tablero(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(0,7), SUR))
        

    def test_no_hay_casilla_vacia_hacia(self):
        t = leer_tablero([
                      '-r----rr', #7
                      '-mrh----', #6
                      '-r---r--', #5
                      'd-EH---c', #4
                      '-M--hD-d', #3
                      '-R-e----', #2
                      '---H-R-C', #1
                      'R-R---RR', #0
                      #01234567
                    ])
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(3,4), ESTE))

class test_hay_pieza_amiga_vecina(unittest.TestCase): #si el coverage da bajo, chequear estos test

    def test_hay_pieza_amiga_vecina(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 3)))

    def test_hay_pieza_amiga_vecina_SUR(self):
            t = leer_tablero([
                  'R-hRD-Rr', #7
                  'M----d--', #6
                  '-h-rrCR-', #5
                  'R-rcE---', #4
                  '--drRR--', #3
                  '-HD-H--m', #2
                  '--r-RCc-', #1
                  're---r--', #0
                  #01234567
                ])
            self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(5, 3)))

    def test_hay_pieza_amiga_vecina_ESTE(self):
                t = leer_tablero([
                      'R-hRD-Rr', #7
                      'M----d--', #6
                      '-h-rrCR-', #5
                      'R-rcE---', #4
                      '---rRR--', #3
                      '-HD-H--m', #2
                      '--r-RCc-', #1
                      're---r--', #0
                      #01234567
                    ])
                self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 2)))

    def test_hay_pieza_amiga_vecina_OESTE(self):
                    t = leer_tablero([
                          'R-hRD-Rr', #7
                          'M----d--', #6
                          '-h-rrCR-', #5
                          'Rcr-E---', #4
                          '---rRR--', #3
                          '-HD-H--m', #2
                          '--r-RCc-', #1
                          're---r--', #0
                          #01234567
                        ])
                    self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 2)))
    
    def test_no_hay_pieza_amiga_vecina(self): 
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_amiga_vecina(t, Posicion(7,7)))       

class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), OESTE))

    def test_no_hay_pieza_enemiga_mas_debil_hacia(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(0,6), NORTE))

    def test_hay_pieza_enemiga_mas_debil_hacia_casilla_vacia(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(0,2), ESTE))

    def test_hay_pieza_enemiga_mas_debil_hacia_fuera_del_tablero(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(0,7), SUR))

class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = leer_tablero([
              'R-e--mRr', #7
              '------dE', #6
              'h--Rr-RR', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

    def test_hay_pieza_enemiga_mas_fuerte_vecina_NORTE(self):
        t = leer_tablero([
                'R-e--mRr', #7
                '------dE', #6
                'h--Rr-RR', #5
                'cC-R-C--', #4
                '-r-HDrr-', #3
                '----rc--', #2
                'h-R-M-R-', #1
                'rr-D-dH-', #0
                #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

    def test_hay_pieza_enemiga_mas_fuerte_vecina_SUR(self):
        t = leer_tablero([
                'R-e--mRr', #7
                '------dE', #6
                'h--Rr-RR', #5
                'c--R-C--', #4
                '-r-HDrr-', #3
                '-C--rc--', #2
                'h-R-M-R-', #1
                'rr-D-dH-', #0
                #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

    def test_hay_pieza_enemiga_mas_fuerte_vecina_OESTE(self):
        t = leer_tablero([
                'R-e--mRr', #7
                '------dE', #6
                'h--Rr-RR', #5
                'c--R-C--', #4
                'Cr-HDrr-', #3
                '----rc--', #2
                'h-R-M-R-', #1
                'rr-D-dH-', #0
                #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

    def test_no_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = leer_tablero([
              'R-e--mRr', #7
              '------dE', #6
              'h--Rr-RR', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t,Posicion(7,0)))

class test_hay_pieza_congelada(unittest.TestCase):

    def test_hay_pieza_congelada(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_congelada(t, Posicion(6, 1)))

    def test_no_hay_pieza_congelada(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(3,3)))

    def test_no_hay_pieza_congelada_pq_es_mas_fuerte(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t,Posicion(3,2)))

    def test_hay_pieza_congelada_en_vacio(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(1,3)))

#### Ejercicio 4

class test_puede_realizar_movimiento(unittest.TestCase):

    def test_es_casilla_vacia(self):
        t = leer_tablero([
            '--eMr---', #7
            '--------', #6
            '-R----r-', #5
            '--------', #4
            '--mMd---', #3
            '---D----', #2
            '--------', #1
            '-mD--mDR', #0
            #01234567
        ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(4, 4), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_mover_a_secas_ok(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

    def test_arrastrar_ok(self):
        t = leer_tablero([
                '--eMr---', #7
                '--------', #6
                '-R----r-', #5
                '------E-', #4
                '--mMd---', #3
                '---D----', #2
                '--------', #1
                '-mD--mDR', #0
                #01234567
            ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(4, 6), [ESTE, SUR])
        self.assertTrue(puede_realizar_movimiento(j, m))

    def test_empujar_ok(self):
        t = leer_tablero([
            '--eMr---', #7
            '--------', #6
            '-R----r-', #5
            '-c------', #4
            '--mMd---', #3
            '---D----', #2
            '--------', #1
            '-mD--mDR', #0
            #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(4, 1), [NORTE, OESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
    
    def test_mover_a_secas_mal(self):
        t = leer_tablero([
            '--eMr---', #7
            '--------', #6
            '-R----r-', #5
            '------M-', #4
            '--mMd---', #3
            '---D----', #2
            '--------', #1
            '-mD--mDR', #0
            #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 6), [SUR])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_arrastrar_mal(self):
        t = leer_tablero([
            '--eMr---', #7
            '--------', #6
            '-R----r-', #5
            '-c----E-', #4
            '--mMd---', #3
            '---D----', #2
            '--------', #1
            '-mD--mDR', #0
            #01234567
            ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(5, 1), [ESTE, NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_empujar_mal(self):
        t = leer_tablero([
            '--eMr---', #7
            '--------', #6
            '-R----r-', #5
            '-c----M-', #4
            '--mMd---', #3
            '---D----', #2
            '--------', #1
            '-mD--mDR', #0
            #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(5, 6), [SUR, ESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_movimiento_conejo_dorado_hacia_atras(self):
        t = leer_tablero([
            'rrrrrrr-', #7
            'ccddhhm-', #6
            '-------r', #5
            '-------e', #4
            '-R------', #3
            '--------', #2
            'EMHHDDCC', #1
            'R-RRRRRR', #0
            #01234567
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(3, 1), [SUR])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_movimiento_conejo_plateado_hacia_atras(self):
        t = leer_tablero([
            'rrrrrrr-', #7
            'ccddhhm-', #6
            '-------r', #5
            '-------e', #4
            '--------', #3
            '--------', #2
            'EMHHDDCC', #1
            'RRRRRRRR', #0
            #01234567
        ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 7), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

#### Ejercicio 5

class test_activar_trampas(unittest.TestCase):

    def test_activar_trampas_ok(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H--m--', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)
        
    def test_activar_trampas_innecesarias(self):
        t0 = leer_tablero([
            '-eRD--rd', #7
            '--------', #6
            'H-------', #5
            '-H--r-Cr', #4
            'R-------', #3
            'R-------', #2
            'R-------', #1
            'c-D---R-', #0
            #01234567
        ])
        t1 = leer_tablero([
            '-eRD--rd', #7
            '--------', #6
            'H-------', #5
            '-H--r-Cr', #4
            'R-------', #3
            'R-------', #2
            'R-------', #1
            'c-D---R-', #0
            #01234567
        ])
        t2 = activar_trampas(t0)
        self.assertEqual(t2, t1)
        
    def test_activar_trampas_casilla_trampa_1(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r-----', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)
        
    def test_activar_trampas_casilla_trampa_2(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H----E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)
            
    def test_activar_trampas_casilla_3(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H-----', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)
    
    def test_activar_trampas_casilla_4(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R----m--', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

    def test_no_activar_trampas_por_amigo(self):
            t0 = leer_tablero([
                '-eRD--rd', #7
                '--------', #6
                'H-rm-E--', #5
                '-H--r-Cr', #4
                'R-------', #3
                'R-H--MR-', #2
                'R-------', #1
                'c-D---R-', #0
                #01234567
                ])
            t1 = leer_tablero([
                '-eRD--rd', #7
                '--------', #6
                'H-rm----', #5
                '-H--r-Cr', #4
                'R-------', #3
                'R----MR-', #2
                'R-------', #1
                'c-D---R-', #0
                #01234567
                ])
            t2 = activar_trampas(t0)
            self.assertNotEqual(t0, t1)
            self.assertEqual(t2, t1)



### Ejercicio 6

class test_realizar_movimiento(unittest.TestCase):
    def test_pasar_de_turno(self):
        t0 = leer_tablero([
                'rrrrrrrr', #7
                'ccddhh-e', #6
                '--------', #5
                '---m----', #4
                '--------', #3
                '--------', #2
                'EMHHDDCC', #1
                'RRRRRRRR', #0
                #01234567
                ])
        tN = leer_tablero([
                'rrrrrrrr', #7
                'ccddhh-e', #6
                '---m----', #5
                '--------', #4
                '--------', #3
                '--------', #2
                'EMHHDDCC', #1
                'RRRRRRRR', #0
                #01234567
                ])
        j0 = Juego(t0, PLATEADO, 3) 
        jN = Juego(tN, DORADO, 0) 
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    def test_mover_a_secas(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---m----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '---m----', #5
               '--------', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, PLATEADO, 0) 
        jN = Juego(tN, PLATEADO, 1) 
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    def test_empujando(self):
        t0 = leer_tablero([
            'rrrrrrrr', #7
            'ccddhhm-', #6
            '--------', #5
            '------e-', #4
            '------C-', #3
            '--------', #2
            'EMHHDDC-', #1
            'RRRRRRRR', #0
            #01234567
        ])
        t1 = leer_tablero([
            'rrrrrrrr', #7
            'ccddhhm-', #6
            '--------', #5
            '--------', #4
            '-----Ce-', #3
            '--------', #2
            'EMHHDDC-', #1
            'RRRRRRRR', #0
            #01234567
        ])
        j0 = Juego(t0, PLATEADO, 0)
        j1 = Juego(t1, PLATEADO, 2)
        mN = Movimiento(EMPUJAR, Posicion(4, 6), [SUR, OESTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), j1)
        
    def test_arrastrando(self):
        t0 = leer_tablero([
            'rrrrrrrr', #7
            'ccddhhm-', #6
            '--------', #5
            '------e-', #4
            '------C-', #3
            '--------', #2
            'EMHHDD-C', #1
            'RRRRRRRR', #0
            #01234567
        ])
        t1 = leer_tablero([
            'rrrrrrrr', #7
            'ccddhhm-', #6
            '--------', #5
            '-----eC-', #4
            '--------', #3
            '--------', #2
            'EMHHDD-C', #1
            'RRRRRRRR', #0
            #01234567
        ])
        j0 = Juego(t0, PLATEADO, 0)
        j1 = Juego(t1, PLATEADO, 2)
        mN = Movimiento(ARRASTRAR, Posicion(4, 6), [OESTE, NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), j1)
        
    def test_moviendo_pieza_mas_fuerte(self):
        t0 = leer_tablero([
            'rrrrrrrr', #7
            'ccddhhm-', #6
            '--------', #5
            '-------e', #4
            '-------C', #3
            '--------', #2
            'EMHHDDC-', #1
            'RRRRRRRR', #0
            #01234567
        ])
        j0 = Juego(t0, DORADO, 0)
        mN = Movimiento(ARRASTRAR, Posicion(3, 7), [NORTE, NORTE])
        self.assertFalse(puede_realizar_movimiento(j0, mN))
        
        
### Ejercicio 7

class test_ganador_del_juego(unittest.TestCase):

    def test_promueve_conejo_dorado_turno_del_oponente(self):
        t = leer_tablero([
              'rr----Rr', #7
              'c-----me', #6
              '---Ed-R-', #5
              '-M---R--', #4
              '---R----', #3
              '-rrrr---', #2
              '-H---DCC', #1
              'R-----RR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)
        
    def test_promueve_conejo_plateado_turno_de_oponente(self):
        t = leer_tablero([
            'rr-----r', #7
            'c-----me', #6
            '---Ed-R-', #5
            '-M---R--', #4
            '---R----', #3
            '-rr-r---', #2
            '-H---DCC', #1
            'R--r--RR', #0
            #01234567
        ])
        j: Juego = Juego(t, DORADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), PLATEADO)
    
    def test_plateado_se_queda_sin_conejos(self):
        t = leer_tablero([
            '--------', #7
            'c-----me', #6
            '---Ed-R-', #5
            '-M---R--', #4
            '---R----', #3
            '--------', #2
            '-H---DCC', #1
            'R-----RR', #0
            #01234567
        ])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)
    
    def test_dorado_se_queda_sin_conejos(self):
        t = leer_tablero([
            'rr-----r', #7
            'c-----me', #6
            '---Ed---', #5
            '-M------', #4
            '--------', #3
            '-rrrr---', #2
            '-H---DCC', #1
            '--------', #0
            #01234567
        ])
        j = Juego(t, DORADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), PLATEADO)
  
    def test_no_hay_ganador_pq_no_promocionaron(self):
        t = leer_tablero([
            '--------', #7
            'c-----me', #6
            '---Ed---', #5
            '-M-rR---', #4
            '--------', #3
            '--------', #2
            '-H---DCC', #1
            '--------', #0
            #01234567
        ])
        j: Juego = Juego(t, DORADO, 0)
        self.assertFalse(hay_ganador_determinado(j))

### Ejercicio Extra

class test_contar_figuras_de_color(unittest.TestCase):
    def test_dict_tablero_inicial_ok(self):
        t = leer_tablero([
        'hcdmedch', #7
        'rrrrrrrr', #6
        '--------', #5
        '--------', #4
        '--------', #3
        '--------', #2
        'RRRRRRRR', #1
        'HCDMEDCH', #0
        #01234567
        ])
        j1:Juego = Juego(t, DORADO, 0)
        j2:Juego = Juego(t, PLATEADO, 0)
        d:dict = {ELEFANTE: 1, CAMELLO: 1, CABALLO: 2, PERRO: 2, GATO: 2, CONEJO: 8}
        for i in d.keys():
            self.assertEqual(d[i], contar_figuras_de_color(j1, PLATEADO)[i])
        for i in d.keys():
            self.assertEqual(d[i], contar_figuras_de_color(j2, PLATEADO)[i])

    def test_dict_tablero_en_juego_ok(self):
        t = leer_tablero([
        '--eMr---', #7
        '--------', #6
        '-R----r-', #5
        '-c------', #4
        '--mMd---', #3
        '---D----', #2
        '--------', #1
        '-mD--mDR', #0
        #01234567
        ])
        j:Juego = Juego(t, PLATEADO, 0)
        d:dict = {ELEFANTE: 1, CAMELLO: 3, GATO: 1, CONEJO: 2}
        for i in d.keys():
            self.assertEqual(d[i], contar_figuras_de_color(j, PLATEADO)[i])

    
class test_puede_promover(unittest.TestCase):
    def test_puede_promover_ok(self):
        t = leer_tablero([
            'rr-----r', #7
            'c---R-me', #6
            '---E----', #5
            '-M--d---', #4
            '--------', #3
            '-rrr----', #2
            '-H--r-CC', #1
            '--------', #0
            #01234567
        ])
        j1:Juego = Juego(t, DORADO, 0)
        j2:Juego = Juego(t, PLATEADO, 0)
        self.assertTrue(puede_promover(j1))
        self.assertTrue(puede_promover(j2))

    def test_no_puede_promover(self):
        t = leer_tablero([
            'rr-----r', #7
            'c---R-me', #6
            '---Ed---', #5
            '-M------', #4
            '--------', #3
            '-rrr----', #2
            '-H--r-CC', #1
            '----R---', #0
            #01234567
        ])
        j1:Juego = Juego(t, DORADO, 0)
        j2:Juego = Juego(t, PLATEADO, 2)
        self.assertFalse(puede_promover(j1))
        self.assertFalse(puede_promover(j2))