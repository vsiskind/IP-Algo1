absoluto :: Integer -> Integer
-- requiere: {True}
-- asegura: {Si n es positivo, devuelve n. Si n es negativo, devuleve (-n)}
absoluto n | n < 0 = (-n)
           | otherwise = n

maximoAbsoluto :: Integer -> Integer -> Integer
-- requiere: {True}
-- asegura: {res es igual al valor absoluto de x o de y}
-- asegura: {res es mayor al valor absoluto de x o de y}
maximoAbsoluto x y | absoluto x >= absoluto y = absoluto x
                   | otherwise = absoluto y

maximo3 :: Integer -> Integer -> Integer -> Integer
-- requiere: {True}
-- asegura: {res es igual a x, o y, o z}
-- asegura: {res es mayor o igual a x, o y, o z}
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | z >= x && z >= y = z

algunoEsCero :: Float -> Float -> Bool
-- requiere: {True}
-- asegura: {devuelve True si x o y o los dos son 0, y devuelve false si no.}
algunoEsCero x y | x == 0 || y == 0 = True
                 | otherwise = False

ambosSonCero :: Float -> Float -> Bool
-- requiere: {x e y son numeros reales}
-- asegura: {devuelve True si ambos x e y son 0, y devuelve false si no.}
ambosSonCero 0 0 = True
ambosSonCero x y = False

enMismoIntervalo :: Float -> Float -> Bool
-- requiere: {True}
-- asegura: {devuelve True si x e y estan en el mismo intervalo de (-inf, 3], o (3, 7], o (7, inf)}
-- asegura: {devuelve False si no estan los dos en el mismo intervalo}
enMismoIntervalo x y | x <= 3 && y <= 3 = True
                     | x > 7 && y > 7 = True
                     | x > 3 && x <= 7 && y > 3 && y <= 7 = True
                     | otherwise = False

sumaDistintos :: Integer -> Integer -> Integer -> Integer
-- requiere: {True}
-- asegura: {devuelve la suma de 3 numeros si todos son distintos}
-- asegura: {si hay repetidos devolver la suma sin repetidos}
sumaDistintos x y z | x /= y && x /= z && y/= z = x + y + z
                    | x /= y && (x == z || y == z) = x + y
                    | x == y && x /= z = x + z
                    | otherwise = x

esMultiploDe :: Integer -> Integer -> Bool
-- requiere: {True}
-- asegura: {si mod x y da 0 devuelve True, si no da 0 devuelve False}
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

digitoUnidades :: Integer -> Integer
-- requiere: {True}
-- asegura: {devuelve el resultado de hacer el resto 10 de x}
digitoUnidades x = x `mod` 10

digitoDecenas :: Integer -> Integer
-- requiere: {x es mayor estricto a 9}
-- asegura: {devuelve el resultado de hacer una division entera por 10}
digitoDecenas x = mod (div x 10) 10