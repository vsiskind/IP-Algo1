
-- Ejercicio 1
-- 1.1)
double:: Int -> Int
double x = x + x

-- 1.2)
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

-- 1.3)
g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

-- 1.4)
h :: Integer -> Integer
-- fog
h num = f (g num)

-- 1.5)
k :: Integer -> Integer
-- gof
k num = f (g num)


-- Ejericio 2
-- 2.1)
absoluto :: Integer -> Integer
-- requiere: {True}
-- asegura: {Si n es positivo, devuelve n. Si n es negativo, devuleve (-n)}
absoluto n | n < 0 = (-n)
           | otherwise = n

-- 2.2)
maximoAbsoluto :: Integer -> Integer -> Integer
-- requiere: {True}
-- asegura: {res es igual al valor absoluto de x o de y}
-- asegura: {res es mayor al valor absoluto de x o de y}
maximoAbsoluto x y | absoluto x >= absoluto y = absoluto x
                   | otherwise = absoluto y

-- 2.3)
maximo3 :: Integer -> Integer -> Integer -> Integer
-- requiere: {True}
-- asegura: {res es igual a x, o y, o z}
-- asegura: {res es mayor o igual a x, o y, o z}
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | z >= x && z >= y = z

-- 2.4)
algunoEsCero :: Float -> Float -> Bool
-- requiere: {True}
-- asegura: {devuelve True si x o y o los dos son 0, y devuelve false si no.}
algunoEsCero x y | x == 0 || y == 0 = True
                 | otherwise = False

-- 2.5)
ambosSonCero :: Float -> Float -> Bool
-- requiere: {x e y son numeros reales}
-- asegura: {devuelve True si ambos x e y son 0, y devuelve false si no.}
ambosSonCero 0 0 = True
ambosSonCero x y = False

-- 2.6)
enMismoIntervalo :: Float -> Float -> Bool
-- requiere: {True}
-- asegura: {devuelve True si x e y estan en el mismo intervalo de (-inf, 3], o (3, 7], o (7, inf)}
-- asegura: {devuelve False si no estan los dos en el mismo intervalo}
enMismoIntervalo x y | x <= 3 && y <= 3 = True
                     | x > 7 && y > 7 = True
                     | x > 3 && x <= 7 && y > 3 && y <= 7 = True
                     | otherwise = False

-- 2.7)
sumaDistintos :: Integer -> Integer -> Integer -> Integer
-- requiere: {True}
-- asegura: {devuelve la suma de 3 numeros si todos son distintos}
-- asegura: {si hay repetidos devolver la suma sin repetidos}
sumaDistintos x y z | x /= y && x /= z && y/= z = x + y + z
                    | x /= y && (x == z || y == z) = x + y
                    | x == y && x /= z = x + z
                    | otherwise = x

-- 2.8)
esMultiploDe :: Integer -> Integer -> Bool
-- requiere: {True}
-- asegura: {si mod x y da 0 devuelve True, si no da 0 devuelve False}
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

-- 2.9)
digitoUnidades :: Integer -> Integer
-- requiere: {True}
-- asegura: {devuelve el resultado de hacer el resto 10 de x}
digitoUnidades x = x `mod` 10

-- 2.10)
digitoDecenas :: Integer -> Integer
-- requiere: {x es mayor estricto a 9}
-- asegura: {devuelve el resultado de hacer una division entera por 10}
digitoDecenas x = mod (div x 10) 10


-- Ejercicio 3
estanRelacionados :: Integer -> Integer -> Bool
-- a*a + a*b*k = 0
--a*b*k = -a^2
--b*k = -a
--b*k = a
-- b es multiplo de a?
estanRelacionados a b = a `mod` b == 0
                      

-- Ejercicio 4
-- 4.1)
productoInterno :: (Float, Float) -> (Float, Float) -> Float
-- requiere: {True}
-- asegura: {devuelve la suma del producto de los enteros en la primer posicion de cada tupla
--           y el producto de los enteros en la segunda posicion de cada tupla.}
productoInterno (a, b) (c, d) = (a * c) + (b * d)

-- 4.2)
esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (a, b) (c, d) = (a < c) && (b < d)

-- 4.3)
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1, y1) (x2, y2) = sqrt((x2 - x1)**2 + (y2 - y1)**2)

-- 4.4)
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x, y, z) = x + y + z

-- 4.5)
sumarsoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarsoloMultiplos (x, y, z) a | (x `mod` a == 0) && (y `mod` a /= 0) && (z `mod` a /= 0) = x
                               | (x `mod` a /= 0) && (y `mod` a == 0) && (z `mod` a /= 0) = y
                               | (x `mod` a /= 0) && (y `mod` a /= 0) && (z `mod` a == 0) = z
                               | (x `mod` a == 0) && (y `mod` a == 0) && (z `mod` a /= 0) = x + y
                               | (x `mod` a == 0) && (y `mod` a /= 0) && (z `mod` a == 0) = x + z
                               | (x `mod` a /= 0) && (y `mod` a == 0) && (z `mod` a == 0) = y + z
                               | (x `mod` a == 0) && (y `mod` a == 0) && (z `mod` a == 0) = x + y + z
                               | otherwise = 0

-- 4.6)
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z) | x `mod` 2 == 0 = 1
                       | y `mod` 2 == 0 = 2
                       | z `mod` 2 == 0 = 3
                       | otherwise = 4

-- 4.7)
crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

-- 4.8)
invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

-- 4.9)
type Punto2D = (Float, Float)

productoInterno2 :: Punto2D -> Punto2D -> Float
productoInterno2 (a, b) (c, d) = (a * c) + (b * d)

esParMenor2 :: Punto2D -> Punto2D -> Bool
esParMenor2 (a, b) (c, d) = (a < c) && (b < d)

distancia2 :: Punto2D -> Punto2D -> Float
distancia2 (x1, y1) (x2, y2) = sqrt((x2 - x1)**2 + (y2 - y1)**2)


-- Ejercicio 5
-- 5.1)
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x, y, z) = (f x > g x) && (f y > g y) && (f z > g z)

-- 5.2)
f1 :: Integer -> Integer
f1 n | n <= 7 = n^2
    | otherwise = 2*n - 1

-- 5.3)
g1 :: Integer -> Integer
g1 n | n `mod` 2 == 0 = n `div` 2
    | otherwise = 3*n + 1


-- Ejercicio 6
type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto a | a `mod` 4 /= 0 = False
           | (a `mod` 100 == 0) && (a `mod` 400 /= 0) = False
           | otherwise = True


-- Ejercicio 7
-- 7.1)
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1, y1, z1) (x2, y2, z2) = abs (x1 - x2) + abs (y1 - y2) + abs (z1 - z2)

-- 7.2)
type Punto3D = (Float, Float, Float)

distanciaManhattan2 :: Punto3D -> Punto3D -> Float
distanciaManhattan2 (x1, y1, z1) (x2, y2, z2) = abs (x1 - x2) + abs (y1 - y2) + abs (z1 - z2)


-- Ejercicio 8
-- 8.1)
comparar :: Integer -> Integer -> Integer
comparar x y | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
             | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
             | otherwise = 0

-- 8.2)
sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = ((abs x) `mod` 10) + (((abs x) `div` 10) `mod` 10)