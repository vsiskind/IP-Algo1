from definiciones import *

#### Algunas funciones ya dadas

def son_posiciones_vecinas(pos1 : Posicion, pos2 : Posicion) -> bool: # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) \
        or (pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1)

def direccion_desde_hasta(pos1 : Posicion, pos2 : Posicion) -> Direccion: # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
       return NORTE
    elif pos1.fila > pos2.fila:
       return SUR
    elif pos1.columna < pos2.columna:
       return ESTE
    else:
       return OESTE

def pasar_turno(j : Juego) -> Juego: # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)

#### Ejercicio 1

def tablero_bien_formado(t : Tablero) -> bool:
    """
    Chequea si el tablero esuna matriz cuadrada
    Requiere:
        Que le pase los parámetros
    PRE:
        True
    Args:
        t (tablero):
        
    Returns:
        True si y solo si el tablero es una matriz cuadrada
    """
    
    bien_formado:bool = True
    if len(t) != ALTO:
        bien_formado = False
    i:int = 0
    while i < len(t) and bien_formado:
        if len(t[i]) != ANCHO:
            bien_formado = False
        i += 1
    return bien_formado

def posicion_en_tablero(pos : Posicion) -> bool:
    """
    Verifica si la fila de una posicion está en [0, ALTO]
    y si la columna está en [0, ANCHO]
    Requiere:
        Que le pase los parámetros

    PRE: True
    Args:
        pos (Posicion): posicion a chequear si es válida
    Returns:
        True si 0 <= pos.fila < ALTO and 0 <= pos.columna < ANCHO
    """
    
    return (0 <= pos.fila < ALTO) and (0 <= pos.columna < ANCHO)

def movimiento_bien_formado(m : Movimiento) -> bool:
    """
    Verifica si el movimiento cumple con las reglas de pasos en movimientos,
    mover_a_secas = 1 paso,
    arrastrar = 2 pasos,
    empujar = 2 pasos.
    Requiere:
        Que le pase los parámetros
    """
    
    bien_formado : bool = False
    if posicion_en_tablero(m.origen):
        if m.accion == MOVER_A_SECAS and len(m.pasos) == 1:
            bien_formado = True
        elif m.accion == ARRASTRAR and len(m.pasos) == 2:
            bien_formado = True
        elif m.accion == EMPUJAR and len(m.pasos) == 2:
            bien_formado = True
    return bien_formado

def juego_bien_formado(j : Juego) -> bool:
    """
    verficia si el tablero es válido (es una matriz cuadrada),
    y si pasos consumidos está en [0, 4]
    Requiere:
        Que le pase los parámetros
    """
    
    bien_formado:bool = True
    if not tablero_bien_formado(j.tablero):
        bien_formado = False
    if 0 > j.pasos_consumidos or j.pasos_consumidos >= 4:
        bien_formado = False
    return bien_formado


#### Ejercicio 2
def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    """
    Devuelve la posicion adyacente a la dada en una dirección dada
    Requiere:
        Que le pase los parámetros
    
    PRE: True
    Args:
        pos (Posicion): posicion donde está la pieza 
        d (Direccion): direccion en la que se mueve
    Returns:
        True si y solo si esPosiciónVecinaHacia
    """
    res: Posicion = Posicion(-1, -1)
    if d == NORTE:
        res = Posicion(pos.fila + 1, pos.columna)
    if d == SUR:
        res = Posicion(pos.fila - 1, pos.columna)
    if d == ESTE:
        res = Posicion(pos.fila, pos.columna + 1)
    if d == OESTE:
        res = Posicion(pos.fila, pos.columna - 1)
    return res

def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    """
    Devuelve los datos de una casilla en específico (si está vacía o si tiene una pieza y, en caso de que haya una, sus datos)
    Requiere:
        Que el tablero sea válido.
        Que la posicion sea dentro del tablero.
    """
    return t[p.fila][p.columna]

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    """
    Devuelve si la casilla de la posición dada está vacía
    Requiere:
        Que el tablero sea válido.
        Que la posicion sea dentro del tablero. 
    """
    return casilla_en_posicion(t, pos) == VACIA  

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    """
    Devuelve si hay una pieza de cierto Color en cierta Posicion
    Requiere:
        Que el tablero sea válido.
        Que la posicion sea dentro del tablero.
    
    PRE:
        tableroBienFormado(t)
        posicionEnTablero(pos)
    Args:
        t (Tablero): Tablero actual
        pos (Posicion): Posicion de una pieza
        col: Color con el cual se verifica
    Returns:
    """
    res : bool = False
    if not hay_casilla_vacia(t, pos):
        res = casilla_en_posicion(t, pos).color == col
    
    return res

def hayFiguraDeColor(t : Tablero, pos : Posicion, f : Figura, col : Color) -> bool:
    res: bool = False

    if  posicion_en_tablero(pos) and \
    not (hay_casilla_vacia(t, pos)) and \
    t[pos.fila][pos.columna].figura == f and \
    t[pos.fila][pos.columna].color == col:
        res = True
    
    return res

#### Ejercicio 3

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Devuelve si la casilla en la posición adyacente a la dada, en la dirección dada está vacía
    Requiere:
        Que el tablero sea válido.
        Que la posicion sea dentro del tablero.

    Args:
        t (Tablero): _description_
        pos (Posicion): _description_
        d (Direccion): _description_

    Returns:
        bool: _description_
    """
    pos_vecina : Posicion = posicion_vecina_hacia(pos, d)
    hay_vacia : bool = False
    if posicion_en_tablero(pos_vecina):
        hay_vacia = hay_casilla_vacia(t, pos_vecina)
    return hay_vacia

#funcion auxiliar
def hay_pieza_amiga_hacia(t:Tablero, pos:Posicion, d:Direccion) -> bool:
    """
    Devuelve si la casilla en la posición adyacente a la dada, en la dirección dada es una pieza amiga (del mismo color)

    Args:
        t (Tablero): _description_
        pos (Posicion): _description_
        d (Direccion): _description_

    Returns:
        bool: _description_
    """
    hay_pieza_amiga:bool = False
    pieza_original: Casilla = casilla_en_posicion(t, pos)
    posicion_amiga : Posicion = posicion_vecina_hacia(pos, d)
    if posicion_en_tablero(posicion_amiga) and not hay_casilla_vacia(t, posicion_amiga):
        pieza_vecina:Casilla = casilla_en_posicion(t, posicion_amiga)
        if pieza_original.color == pieza_vecina.color:
            hay_pieza_amiga = True
    return hay_pieza_amiga

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    """
    Devuelve si hay una pieza amiga (del mismo color a la dada) en alguna de las casillas adyacentes
    """
    hay_pieza_amiga:bool = False
    if hay_pieza_amiga_hacia(t, pos, NORTE):
        hay_pieza_amiga = True
    elif hay_pieza_amiga_hacia(t, pos, SUR):
        hay_pieza_amiga = True
    elif hay_pieza_amiga_hacia(t, pos, ESTE):
        hay_pieza_amiga = True
    elif hay_pieza_amiga_hacia(t, pos, OESTE):
        hay_pieza_amiga = True
    return hay_pieza_amiga

#Auxiliar
def hay_pieza_enemiga_en_pos(t : Tablero, pos : Posicion, col_propio : Color) -> bool:
    """
    Devuelve si hay una pieza enemiga (del otro color) en una posicion dada

    Args:
        t (Tablero): _description_
        pos (Posicion): _description_
        col_propio (Color): _description_

    Returns:
        bool: _description_
    """
    hay_pieza_enemiga = False
    if not hay_casilla_vacia(t, pos):
        hay_pieza_enemiga = not hay_pieza_de_color(t, pos, col_propio)
    return hay_pieza_enemiga

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Devuelve si en la posicion adyacente a la dada en la dirección dada hay una pieza enemiga (otro color) más débil 
    (dependiendo de las relaciones de fuerza en definiciones)
    Requiere:
        Que el tablero sea válido.
        Que la posicion sea dentro del tablero.
        Que haya una pieza en la posición dada.
    """
    hay_pieza_enemiga_debil : bool = False
    pieza_original : Casilla = casilla_en_posicion(t,pos)
    posicion_enemiga:Posicion = posicion_vecina_hacia(pos, d)
    if posicion_en_tablero(posicion_enemiga) and hay_pieza_enemiga_en_pos(t, posicion_enemiga, pieza_original.color):
        pieza_enemiga = casilla_en_posicion(t, posicion_enemiga)
        hay_pieza_enemiga_debil = fuerza(pieza_original.figura) > fuerza(pieza_enemiga.figura)
    return hay_pieza_enemiga_debil

#Auxiliar
def hay_pieza_enemiga_mas_fuerte_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Devuelve si hay una pieza enemiga (otro color) más fuerte (dependiendo de las relaciones de fuerza en definiciones) en una dirección dada
    Requiere:
        Que el tablero sea válido.
        Que la posicion sea dentro del tablero.
        Que haya una pieza en la posición dada.

    Args:
        t (Tablero): _description_
        pos (Posicion): _description_
        d (Direccion): _description_

    Returns:
        bool: _description_
    """
    hay_pieza_enemiga_fuerte : bool = False
    pos_enemiga : Posicion = posicion_vecina_hacia(pos, d)
    pieza_original : Casilla = casilla_en_posicion(t, pos)
    if posicion_en_tablero(pos_enemiga) and hay_pieza_enemiga_en_pos(t, pos_enemiga, pieza_original.color):
        pieza_enemiga : Casilla = casilla_en_posicion(t, pos_enemiga)
        hay_pieza_enemiga_fuerte = fuerza(pieza_enemiga.figura) > fuerza(pieza_original.figura)
    return hay_pieza_enemiga_fuerte

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    """
    Devuelve si en alguna de las posiciones adyacentes hay una pieza enemiga (otro color) más fuerte (dependiendo de las relaciones de fuerza en definiciones)
    Requiere:
        Que el tablero sea válido.
        Que la posicion sea dentro del tablero.
        Que haya una pieza en la posición dada.

    Args:
        t (Tablero): _description_
        pos (Posicion): _description_

    Returns:
        bool: _description_
    """
    hay_pieza_enemiga_fuerte : bool = False
    if hay_pieza_enemiga_mas_fuerte_hacia(t, pos, NORTE):
        hay_pieza_enemiga_fuerte = True
    elif hay_pieza_enemiga_mas_fuerte_hacia(t, pos, SUR):
        hay_pieza_enemiga_fuerte = True
    elif hay_pieza_enemiga_mas_fuerte_hacia(t, pos, ESTE):
        hay_pieza_enemiga_fuerte = True
    elif hay_pieza_enemiga_mas_fuerte_hacia(t, pos, OESTE):
        hay_pieza_enemiga_fuerte = True
    return hay_pieza_enemiga_fuerte

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    """
    Devuelve si hay una pieza congelada en una posición dada.
    Requiere:
        Que el tablero sea válido.
        Que la posicion sea dentro del tablero.

    Args:
        t (Tablero): _description_
        pos (Posicion): _description_

    Raises:
        Exception: _description_

    Returns:
        bool: _description_
    """
    hay_congelada = False
    if not hay_casilla_vacia(t, pos):
        if hay_pieza_enemiga_mas_fuerte_vecina(t,pos) and not hay_pieza_amiga_vecina(t, pos):
            hay_congelada = True
    return hay_congelada

#### Ejercicio 4

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    """
    Verifica si una ficha se puede mover de una casilla a otra.
    Requiere:
        Que el tablero sea válido y la última jugada no haya sido de más de 4 pasos.
        Que el moviemiento corresponda con la cantidad de pasos.
    
    PRE:
        juegoBienFormado(j)
        movimientoBienFormado(m)
    Args:
        j (Juego):
        m (Movimiento)
    Returns:
        True si y solo si puedeRealizarMovimiento(j, m)
    """
    res:bool = False
    if not hay_casilla_vacia(j.tablero, m.origen):
        pieza_color:bool = hay_pieza_de_color(j.tablero, m.origen, j.turno)
        pieza_congelada:bool = hay_pieza_congelada(j.tablero, m.origen)
        direccion_habilitada:bool = direccionDeMovimientoHabilitada(j.tablero, m.origen, m.pasos[0])
        accion_valida:bool = puedeRealizarAccion(j.tablero, m)
        no_max_pasos:bool = j.pasos_consumidos + len(m.pasos) <= MAX_PASOS
        res = pieza_color and not(pieza_congelada) and direccion_habilitada and accion_valida and no_max_pasos
    return res

def direccionDeMovimientoHabilitada(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    direccion_habilitada:bool = True
    casilla:Casilla = casilla_en_posicion(t, pos)
    f:Figura = casilla.figura
    col:Color = casilla.color

    if f == CONEJO and col == DORADO and d == SUR:
        direccion_habilitada = False
    elif f == CONEJO and col == PLATEADO and d == NORTE:
        direccion_habilitada = False

    return direccion_habilitada

def puedeRealizarAccion(t : Tablero, m : Movimiento) -> bool:
    es_posible:bool = True
    accion:Accion = m.accion

    if accion == ARRASTRAR:
        if not(puedeArrastrar(t, m.origen, m.pasos[0], m.pasos[1])):
            es_posible = False
    elif accion == EMPUJAR:
        if not(puedeEmpujar(t, m.origen, m.pasos[0], m.pasos[1])):
            es_posible = False
    else:
        if not(puedeMoverASecas(t, m.origen, m.pasos[0])):
            es_posible = False

    return es_posible

def puedeMoverASecas(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    return hay_casilla_vacia_hacia(t, pos, d)

def puedeArrastrar(t : Tablero, pos : Posicion, d : Direccion, dArrastre : Direccion) -> bool:
    casilla_vacia:bool = hay_casilla_vacia_hacia(t, pos, d)
    enemigo_mas_debil:bool = hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(dArrastre))
    return casilla_vacia and enemigo_mas_debil

def puedeEmpujar(t : Tablero, pos : Posicion, d : Direccion, dEmpuje : Direccion) -> bool:
    enemigo_mas_debil:bool = hay_pieza_enemiga_mas_debil_hacia(t, pos, d)
    pos_enemiga:Posicion = posicion_vecina_hacia(pos, d)
    casilla_vacia:bool = hay_casilla_vacia_hacia(t, pos_enemiga, dEmpuje)
    return enemigo_mas_debil and casilla_vacia
    


#### Ejercicio 5

def activar_trampas(t : Tablero) -> Tablero:
    """
    Devuelve el estado del tablero luego de accionar las trampas (casillas trampas)
    Requiere:
        Que el tablero sea válido y el último juego no haya sido de mas de 4 pasos
    
    PRE:
        tableroBienFormado(t)
        
    Args:
        t (Tablero):
        
    Return:
        res = esTableroDespuesDeActivarTodasLasTrampas(t)
        res cumple tableroBienFormado
    """
    return esTableroDespuesDeActivarTodasLasTrampas(t)

def esTableroDespuesDeActivarTodasLasTrampas(t0 : Tablero) -> Tablero:
    t_copy:Tablero = []
    for fila in t0:
        t_copy.append(fila.copy())
    t_intermedio_1:Tablero = esTableroDespuesDeActivarTrampa(t0, t_copy, POSICIONES_TRAMPA[0])
    t_intermedio_2:Tablero = esTableroDespuesDeActivarTrampa(t_copy, t_intermedio_1, POSICIONES_TRAMPA[1])
    t_intermedio_3:Tablero = esTableroDespuesDeActivarTrampa(t_intermedio_1, t_intermedio_2, POSICIONES_TRAMPA[2])
    t1:Tablero = esTableroDespuesDeActivarTrampa(t_intermedio_2, t_intermedio_3, POSICIONES_TRAMPA[3])
    return t1

def esTableroDespuesDeActivarTrampa(t0 : Tablero, t1 : Tablero, posTrampa : Posicion) -> Tablero:
    if not hay_casilla_vacia(t0, posTrampa):
        if not(hay_pieza_amiga_vecina(t0, posTrampa)):
            esTableroSacandoPieza(t1, posTrampa)
    return t1

def esTableroSacandoPieza(t1 : Tablero, pos : Posicion):
    t1[pos.fila][pos.columna] = VACIA


#### Ejercicio 6

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    """
    Devuelve el nuevo estado del Juego luego de que un jugador haya movido una pieza
    Requiere:
        Que el tablero sea válido y el movimiento también sea válido (el tipo de movimiento corresponde con la cantidad de pasos).
        Que el moviento esté permiido (puede_realizar_movimiento).
            
    PRE:
        juegoBienFormado(j) and movimientoBienFormado(m)
        puedeRealizarMoviento(j, m)
    
    Args:
        j (Juego):
        m (Movimiento):
    
    Returns:
        res cumple juegoBienFormado
        res = juegoPostMovimiento(j, m)
    """
    t_despues_de_movimiento:Tablero = []
    for fila in j.tablero:
        t_despues_de_movimiento.append(fila.copy())
    j1:Juego = Juego(t_despues_de_movimiento, j.turno, j.pasos_consumidos)
    return juegoPostMovimiento(j1, m)
    

def juegoPostMovimiento(j1 : Juego, m : Movimiento) -> Juego:
    t2:Tablero = tableroPostMovimiento(j1.tablero, m)
    j2:Juego = Juego(t2, j1.turno, j1.pasos_consumidos)
    j2 = juegoConTurnoPosiblementeAvanzado(j1, j2, m)
    return j2


def juegoConTurnoPosiblementeAvanzado(j0 : Juego, j1 : Juego, m : Movimiento) -> Juego:
    if hayQueCambiarDeTurno(j0, m):
        j1 = pasar_turno(j1)
    else:
        j1 = Juego(j1.tablero, j0.turno, j0.pasos_consumidos + len(m.pasos))

    return j1

def hayQueCambiarDeTurno(j : Juego, m : Movimiento) -> bool:
    return j.pasos_consumidos + len(m.pasos) == MAX_PASOS


def tableroPostMovimiento(t1 : Tablero, m : Movimiento) -> Tablero:
    if m.accion == ARRASTRAR:
        t1 = tableroPostArrastrar(t1, m.origen, m.pasos[0], m.pasos[1])
    elif m.accion == EMPUJAR:
        t1 = tableroPostEmpujar(t1, m.origen, m.pasos[0], m.pasos[1])
    else:
        t1 = tableroPostMoverASecas(t1, m.origen, m.pasos[0])

    return t1

def tableroPostMoverASecas(t1 : Tablero, pos : Posicion, d : Direccion) -> Tablero:
    posDestino:Posicion = posicion_vecina_hacia(pos, d)
    t1 = esTableroTrasladandoPieza(t1, pos, posDestino)
    t1 = activar_trampas(t1)
    return t1

def tableroPostArrastrar(t1 : Tablero, pos : Posicion, d : Direccion, dArrastre : Direccion) -> Tablero:
    posDestino:Posicion = posicion_vecina_hacia(pos, d)
    posEnemigo:Posicion = posicion_vecina_hacia(pos, opuesta(dArrastre))
    t1 = esTableroTrasladandoPieza(t1, pos, posDestino)
    t1 = esTableroTrasladandoPieza(t1, posEnemigo, pos)
    t1 = activar_trampas(t1)
    return t1

def tableroPostEmpujar(t1 : Tablero, pos : Posicion, d : Direccion, dEmpuje : Direccion) -> Tablero:
    posEnemigo:Posicion = posicion_vecina_hacia(pos, d)
    posHueco:Posicion = posicion_vecina_hacia(posEnemigo, dEmpuje)
    t1 = esTableroTrasladandoPieza(t1, posEnemigo, posHueco)
    t1 = esTableroTrasladandoPieza(t1, pos, posEnemigo)
    t1 = activar_trampas(t1)
    return t1

def esTableroTrasladandoPieza(t : Tablero, posOrigen : Posicion, posDestino : Posicion) -> Tablero:
    casilla_origen:Casilla = casilla_en_posicion(t, posOrigen)
    f:Figura = casilla_origen.figura
    col:Color = casilla_origen.color
    t1:Tablero = []
    for fila in t:
        t1.append(fila.copy())
    esTableroSacandoPieza(t1, posOrigen)
    esTableroPoniendoPieza(t1, posDestino, f, col)
    return t1


def esTableroPoniendoPieza(t1 : Tablero, pos : Posicion, f : Figura, col : Color):
    t1[pos.fila][pos.columna] = Pieza(f, col)

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    """
    Determina si hay un ganador sea cuál sea.
    Requiere:
        Que el tablero sea válido.
        Que la última jugada no haya hecho mas de 4 pasos.
    
    PRE: juegoBienFormado(j)
    
    Args::
        j (Juego): tablero actual del juego
    
    Returns:
        True si y solo si hayGanadorDeterminado(j)
    """
    
    return hayGanadorDeterminado(j)

# auxiliares
def esInicioDeTurno(j: Juego, col: Color) -> bool:
    return (j.pasos_consumidos == 0) and (j.turno == col)

def hayConejoEnTablero(j: Juego, col: Color) -> bool:
    res: bool = False
    for fila in range(len(j.tablero)):
        for columna in range(len(j.tablero[0])):
            if hayFiguraDeColor(j.tablero, Posicion(fila, columna), CONEJO, col):
                res = True
    return res

def posicionEnFilaInicial(pos: Posicion, col: Color) -> bool:
    res: bool = False
    if col == DORADO and pos.fila == 0:
        res = True
    elif col == PLATEADO and pos.fila == 7:
        res = True
    return res

def hayConejoEnFilaInicialOponente(j: Juego, col: Color) -> bool:
    res: bool = False
    for fila in range(len(j.tablero)):
        for columna in range(len(j.tablero[0])):
            if posicionEnFilaInicial(Posicion(fila, columna), oponente(col)) and hayFiguraDeColor(j.tablero, Posicion(fila, columna), CONEJO, col):
                res = True
    return res

def reuneCondicionesDeGanar(j: Juego, col: Color) -> bool:
    return hayConejoEnFilaInicialOponente(j, col) or not (hayConejoEnTablero(j, oponente(col))) 

def reuneCondicionesDeGanarExclusivas(j: Juego, col: Color) -> bool:
    return reuneCondicionesDeGanar(j, col) and not(reuneCondicionesDeGanar(j, oponente(col)))

def esJugadorGanador(j: Juego, col: Color) -> bool:
    res: bool = False
    if (esInicioDeTurno(j, oponente(col)) and reuneCondicionesDeGanar(j, col)) or \
       (esInicioDeTurno(j, col) and reuneCondicionesDeGanarExclusivas(j, col)):
        res = True
    return res 

def hayGanadorDeterminado(j: Juego) -> bool:
    res: bool = False
    if esJugadorGanador(j, DORADO) or esJugadorGanador(j, PLATEADO):
        res = True
    return res

def ganador_del_juego(j : Juego) -> Color | None:
    """
    Determina quien ganó el juego.
    Requiere:
        Que haya un ganador.
        Que el tablero sea válido.
        Que la última jugada no haya hecho mas de 4 pasos.
    
    PRE:
        juegoBienFormado(j)
        hayGanadorDeterminado(j)
        
    Args:
        j (Juego): Estado actual del juego
        
    Returns
        Dorado si y solo si esJugadorGanador(j, DORADO)
        PLATEADO si y solo si esJugadorGanador(j, PLATEADO)
    """
    ganador: Color | None = None
    if esJugadorGanador(j, DORADO):
        ganador = DORADO
    if esJugadorGanador(j, PLATEADO):
        ganador = PLATEADO
    return ganador
    

# ejercicios extras
def contar_figuras_de_color(j: Juego, col: Color) -> dict[Figura, int]:
    """
    Cuenta cuantas piezas de cada tipo le quedan a un jugador determinado.
    Requiere:
        un tablero cuadrado
        Que los pasas previamente dados esten entre 0 y 4 inclusive 
    """
    res: dict[Figura, int] = dict()
    for fila in range(len(j.tablero)):
        for columna in range(len(j.tablero[0])):
            if not hay_casilla_vacia(j.tablero, Posicion(fila, columna)):
                pieza: Pieza = j.tablero[fila][columna]
                if pieza.color == col:
                    if not pieza.figura in res:
                        res[pieza.figura] = 0
                    res[pieza.figura] += 1

    return res

#Ej 2 Extra:
def jugadorActualPuedePromover(j:Juego)-> bool:
    puede_promover : bool = False
    i : int = 0
    mov : Movimiento
    if j.turno == DORADO:
        while i < len(j.tablero) and not puede_promover:
            mov = Movimiento(MOVER_A_SECAS, Posicion(6, i), [NORTE])
            if puede_realizar_movimiento(j, mov):
                puede_promover = hayConejoEnFilaInicialOponente(juegoPostMovimiento(j, mov), j.turno)
            i += 1
    else:
        while i < len(j.tablero) and not puede_promover:
            mov = Movimiento(MOVER_A_SECAS, Posicion(1, i), [SUR])
            if puede_realizar_movimiento(j, mov):
                puede_promover = hayConejoEnFilaInicialOponente(juegoPostMovimiento(j, mov), j.turno)
            i += 1

    return puede_promover

def puede_promover(j:Juego)-> bool:
    return jugadorActualPuedePromover(j)