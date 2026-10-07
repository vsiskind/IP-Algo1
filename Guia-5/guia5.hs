
-- Ejercicio 1)
-- 1.1)
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- 1.2)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

-- 1.3)
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

-- 1.4)
reverso :: [t] -> [t]
reverso [] = []
reverso x = ultimo x : reverso(principio x)


-- Ejercicio 2)
-- 2.1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece t (x:xs) | t == x = True
                   | (x:xs) == [x] = False
                   | otherwise = pertenece t xs

-- 2.2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:xs) | xs == [] = True
                    | igualAlProximo x xs = todosIguales xs
                    | otherwise = False

igualAlProximo :: (Eq t) => t -> [t] -> Bool
igualAlProximo t (x:xs) = t == x

todosIguales2 :: (Eq t) => [t] -> Bool
todosIguales2 (x:y:xs) | xs == [] && x == y = True
                       | x == y = todosIguales2(y:xs)
                       | otherwise = False

-- 2.3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | xs == [] = True
                      | esDistintoDesde x (xs) = todosDistintos (xs)
                      | otherwise = False

esDistintoDesde :: (Eq t) => t -> [t] -> Bool
esDistintoDesde t (x:xs) | xs == [] && t /= x = True
                         | t /= x = esDistintoDesde t (xs)
                         | otherwise = False

-- 2.4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | xs == [] = False
                    | chequeoRepetidos x xs = True
                    | otherwise = hayRepetidos xs

chequeoRepetidos :: (Eq t) => t -> [t] -> Bool
chequeoRepetidos t (x:xs) | t == x = True
                          | xs == [] = False
                          | otherwise = chequeoRepetidos t xs

-- 2.5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar n (x:xs) | xs == [] && x /= n = [x]
                | n == x = xs
                | n /= x = x : quitar n xs

-- 2.6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n l | quitar n l == l = l
                | otherwise = quitarTodos n (quitar n l)

-- 2.7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)

-- 2.8)
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos x y = mismosElementosLista x y && mismosElementosLista y x

mismosElementosLista :: (Eq t) => [t] -> [t] -> Bool
mismosElementosLista (x:xs) y | xs == [] && pertenece x y = True
                              | pertenece x y = mismosElementosLista xs y
                              | otherwise = False

-- 2.9)
capicua :: (Eq t) => [t] -> Bool
capicua x = x == reverso x


-- Ejercicio 3)
-- 3.1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- 3.2)
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

-- 3.3)
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x > maximo xs = x
              | otherwise = maximo xs

-- 3.4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (x+n) : sumarN n xs

-- 3.5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 3.6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo x = sumarN (ultimo x) x 

-- 3.7)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | x `mod` 2 == 0 = x : pares xs
             | otherwise = pares xs

-- 3.8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | x `mod` n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

-- 3.9)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar x = minimo x : ordenar (quitar (minimo x) x)

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:xs) | x < minimo xs = x
              | otherwise = minimo xs


-- Ejercicio 4)
-- 4.1)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
                               | otherwise = x : sacarBlancosRepetidos (y:xs)

-- 4.2)
contarPalabras :: [Char] -> Integer
contarPalabras [] = 1
contarPalabras (x:xs) | x == ' ' = 1 + contarPalabras xs
                      | otherwise = contarPalabras xs

--4.3)
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras x = agruparPalabra x : palabras (quitarPrimeraPalabra x)

agruparPalabra :: [Char] -> [Char]
agruparPalabra [] = []
agruparPalabra (x:xs) | x /= ' ' = x : agruparPalabra xs
                      | otherwise = []

quitarPrimeraPalabra :: [Char] -> [Char]
quitarPrimeraPalabra [] = []
quitarPrimeraPalabra (x:xs) | x /= ' ' = quitarPrimeraPalabra xs
                            | otherwise = xs

-- 4.4)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga x | longitud(head(palabras x)) >= longitud(palabraMasLarga(quitarPrimeraPalabra x)) = head(palabras x)
                  | otherwise = palabraMasLarga(quitarPrimeraPalabra x)

-- 4.5)
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar ((x:[]):xs) = x : aplanar xs
aplanar ((x:y):xs) = x : aplanar (y:xs)
              
aplanar2 :: [[Char]] -> [Char]
aplanar2 [] = []
aplanar2 (x:xs) = aplanarPalabra x  ++ [' '] ++  aplanar2 xs

aplanarPalabra :: [Char] -> [Char]
aplanarPalabra [] = []
aplanarPalabra (x:xs) = x : aplanarPalabra xs

-- 4.6)
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos ((x:[]):[]) = [x]
aplanarConBlancos ((x:[]):xs) = x : ' ' : aplanarConBlancos xs
aplanarConBlancos ((x:y):xs) = x : aplanarConBlancos (y:xs)

-- 4.7)
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos ((x:[]):[]) _ = [x]
aplanarConNBlancos ((x:[]):xs) n = x : nBlancos n ++ aplanarConNBlancos xs n
aplanarConNBlancos ((x:y):xs) n = x : aplanarConNBlancos (y:xs) n

nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos n = ' ' : nBlancos (n-1)


-- Ejercicio 5)
-- 5.1)
sumaAcumulada :: [Integer] -> [Integer]
sumaAcumulada [] = []
sumaAcumulada [x, y] = x : [x+y]
sumaAcumulada (x:y:xs) = x : sumaAcumulada (x+y :xs)

-- 5.2)
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (descomponerPrimo x 2) : descomponerEnPrimos xs

descomponerPrimo :: Integer -> Integer -> [Integer]
descomponerPrimo x p | esPrimo x = [x]
                     | x `mod` p == 0 = p : descomponerPrimo (x `div` p) p
                     | otherwise = descomponerPrimo x (siguientePrimo p)
                     where
                        menorDivisor 1 = 1
                        menorDivisor n = menorDivisorDesde n 2
                        
                        menorDivisorDesde d a | d `mod` a == 0 = a
                                              | otherwise = menorDivisorDesde d (a+1)

                        esPrimo p | p == 1 = False
                                  | otherwise = p == menorDivisor p

                        siguientePrimo n | esPrimo (n+1) = n+1
                                         | otherwise = siguientePrimo (n+1)


-- Ejercicio 6)
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

-- 6.1)
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((n, t):xs) | nombre == n = True
                             | otherwise = enLosContactos nombre xs

-- 6.2)
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto (n1, t1) [] = [(n1, t1)]
agregarContacto (n1, t1) ((n, t):xs) | n1 == n = (n1, t1) : xs
                                     | otherwise = (n, t) : agregarContacto (n1, t1) xs

-- 6.3)
eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto nombre ((n, t):xs) | nombre == n = xs
                                    | otherwise = (n, t) : eliminarContacto nombre xs


--Ejercicio 7)
type Identificacion = Integer
type Ubicacion = Texto
type Disponibilidad = Bool
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]

-- 7.1)
existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker num ((identificacion, estado):xs) 
    | num == identificacion = True
    | otherwise = existeElLocker num xs

-- 7.2)
ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker num ((identificacion, (disponibilidad, ubicacion)):xs)
    | num == identificacion = ubicacion
    | otherwise = ubicacionDelLocker num xs

--7.3)
estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker num ((identificacion, (disponibilidad, ubicacion)):xs)
    | num == identificacion && disponibilidad = True
    | num == identificacion && not(disponibilidad) = False
    | otherwise = estaDisponibleElLocker num xs

-- 7.4)
ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker num ((identificacion, (disponibilidad, ubicacion)):xs)
    | num == identificacion && not(disponibilidad) = (identificacion, (True, ubicacion)) : xs
    | otherwise = (identificacion, (disponibilidad, ubicacion)) : ocuparLocker num xs


-- Ejercicio 8)
--8.1)
sumaTotal :: [[Integer]] -> Integer
sumaTotal [] = 0
sumaTotal (x:xs) = sumaFilas x + sumaTotal xs 

sumaFilas :: [Integer] -> Integer
sumaFilas [] = 0
sumaFilas (x:xs) = x + sumaFilas xs

-- 8.2)
cantidadDeApariciones :: Integer -> [[Integer]] -> Integer
cantidadDeApariciones _ [] = 0
cantidadDeApariciones e (x:xs) = sumaApariciones e x + cantidadDeApariciones e xs

sumaApariciones :: Integer -> [Integer] -> Integer
sumaApariciones e [] = 0
sumaApariciones e (x:xs) | e == x = 1 + sumaApariciones e xs
                         | otherwise = sumaApariciones e xs

-- 8.3)
contarPalabras8 :: String -> [[String]] -> Integer
contarPalabras8 _ [] = 0
contarPalabras8 p (x:xs) = contarPalabrasFilas p x + contarPalabras8 p xs

contarPalabrasFilas :: String -> [String] -> Integer
contarPalabrasFilas _ [] = 0
contarPalabrasFilas p (x:xs) | p == x = 1 + contarPalabrasFilas p xs
                             | otherwise = contarPalabrasFilas p xs

-- 8.4)
cantidadDeApariciones2 :: (Eq a) => a -> [[a]] -> Integer
cantidadDeApariciones2 _ [] = 0
cantidadDeApariciones2 s ([]:xs) = cantidadDeApariciones2 s xs
cantidadDeApariciones2 s ((x:y):xs) | s == x = 1 + cantidadDeApariciones2 s (y:xs)
                                    | otherwise = cantidadDeApariciones2 s (y:xs)

-- 8.5)
multiplicarPorEscalar :: Integer -> [[Integer]] -> [[Integer]]
multiplicarPorEscalar _ [] = []
multiplicarPorEscalar n (x:xs) = multiplicarPorEscalarFilas n x : multiplicarPorEscalar n xs

multiplicarPorEscalarFilas :: Integer -> [Integer] -> [Integer]
multiplicarPorEscalarFilas _ [] = []
multiplicarPorEscalarFilas n (x:xs) = (n * x) : multiplicarPorEscalarFilas n xs

-- 8.6)
concatenarFilas :: [[String]] -> [String]
concatenarFilas [] = []
concatenarFilas (x:xs) = concatenarStrings x : concatenarFilas xs

concatenarStrings :: [String] -> String
concatenarStrings [] = []
concatenarStrings (x:xs) = x ++ concatenarStrings xs

-- 8.7)
iesimaFila :: Integer -> [[a]] -> [a]
iesimaFila j matriz = contarFilas matriz 0 j

contarFilas :: [[a]] -> Integer -> Integer -> [a]
contarFilas (x:xs) i j | i == j = x
                       | otherwise = contarFilas xs (i+1) j

-- 8.8)
iesimaColumna :: Integer -> [[a]] -> [a]
iesimaColumna _ [] = []
iesimaColumna c (x:xs) = contarColumna 0 c x : iesimaColumna c xs

contarColumna :: Integer -> Integer -> [a] -> a
contarColumna i c (x:xs) | i == c = x
                         | otherwise = contarColumna (i+1) c xs

-- 8.9)
matrizIdentidad :: Integer -> [[Integer]]
matrizIdentidad n = generarMatrizIdentidad n 1

generarMatrizIdentidad :: Integer -> Integer -> [[Integer]]
generarMatrizIdentidad n i | i > n = []
                           | otherwise = generarFilaIdentidad n i 1 : generarMatrizIdentidad n (i+1)

generarFilaIdentidad :: Integer -> Integer -> Integer -> [Integer]
generarFilaIdentidad n i j | j == n && j == i = [1]
                           | j == n && j /= i = [0]
                           | j == i = 1 : generarFilaIdentidad n i (j+1)
                           | otherwise = 0 : generarFilaIdentidad n i (j+1)

-- 8.10)
cantidadParesColumna :: Integer -> [[Integer]] -> Integer
cantidadParesColumna _ [] = 0
cantidadParesColumna c (x:xs) | esParColumna 0 c x = 1 + cantidadParesColumna c xs
                              | otherwise = cantidadParesColumna c xs

esParColumna :: Integer -> Integer -> [Integer] -> Bool
esParColumna i c (x:xs) | i == c = x `mod` 2 == 0
                        | otherwise = esParColumna (i+1) c xs

-- 8.11 (Bonus))
multiplicarFilas :: [[Integer]] -> [Integer]
multiplicarFilas [x] = [productoriaFila x]
multiplicarFilas (x:xs) = productoriaFila x : multiplicarFilas xs

productoriaFila :: [Integer] -> Integer
productoriaFila [] = 1
productoriaFila (x:xs) = x * productoriaFila (xs)