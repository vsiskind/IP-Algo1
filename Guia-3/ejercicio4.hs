import System.Console.Haskeline (Interrupt)
productoInterno :: (Float, Float) -> (Float, Float) -> Float
-- requiere: {True}
-- asegura: {devuelve la suma del producto de los enteros en la primer posicion de cada tupla
--           y el producto de los enteros en la segunda posicion de cada tupla.}
productoInterno (a, b) (c, d) = (a * c) + (b * d)

esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (a, b) (c, d) = (a < c) && (b < d)

distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1, y1) (x2, y2) = sqrt((x2 - x1)**2 + (y2 - y1)**2)

sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x, y, z) = x + y + z

sumarsoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarsoloMultiplos (x, y, z) a | (x `mod` a == 0) && (y `mod` a /= 0) && (z `mod` a /= 0) = x
                               | (x `mod` a /= 0) && (y `mod` a == 0) && (z `mod` a /= 0) = y
                               | (x `mod` a /= 0) && (y `mod` a /= 0) && (z `mod` a == 0) = z
                               | (x `mod` a == 0) && (y `mod` a == 0) && (z `mod` a /= 0) = x + y
                               | (x `mod` a == 0) && (y `mod` a /= 0) && (z `mod` a == 0) = x + z
                               | (x `mod` a /= 0) && (y `mod` a == 0) && (z `mod` a == 0) = y + z
                               | (x `mod` a == 0) && (y `mod` a == 0) && (z `mod` a == 0) = x + y + z
                               | otherwise = 0

posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z) | x `mod` 2 == 0 = 1
                       | y `mod` 2 == 0 = 2
                       | z `mod` 2 == 0 = 3
                       | otherwise = 4

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

type Punto2D = (Float, Float)

productoInterno2 :: Punto2D -> Punto2D -> Float
productoInterno2 (a, b) (c, d) = (a * c) + (b * d)

esParMenor2 :: Punto2D -> Punto2D -> Bool
esParMenor2 (a, b) (c, d) = (a < c) && (b < d)

distancia2 :: Punto2D -> Punto2D -> Float
distancia2 (x1, y1) (x2, y2) = sqrt((x2 - x1)**2 + (y2 - y1)**2)
