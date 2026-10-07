module SolucionT2 where

-- Ejercicio 1
f1 :: Integer -> Integer -> Integer
f1 x y | x > y = 0
       | esAbundante x = 1 + f1 (x+1) y
       | otherwise = f1 (x+1) y

esAbundante :: Integer -> Bool
esAbundante n = sumaDivisoresPropios n 1 > n

sumaDivisoresPropios :: Integer -> Integer -> Integer
sumaDivisoresPropios n i | i == n = 0
                         | mod n i == 0 = i + sumaDivisoresPropios n (i+1)
                         | otherwise = sumaDivisoresPropios n (i+1)

-- Ejercicio 2
f2 :: [(String, Integer, Integer)] -> [String]
f2 x = eliminarRepetidos (listaMateriasVencidas x)

listaMateriasVencidas :: [(String, Integer, Integer)] -> [String]
listaMateriasVencidas [] = []
listaMateriasVencidas ((m, a, q):xs) | xs == [] && not(materiaVencida (m, a, q)) = []
                                     | materiaVencida (m, a, q) = m : f2 xs
                                     | otherwise = f2 xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n /= x = x : quitarTodos n xs
                     | otherwise = quitarTodos n xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)

materiaVencida :: (String, Integer, Integer) -> Bool
materiaVencida (m, a, q) | a < 2021 = True
                         | (a == 2021) && (q < 2) = True
                         | otherwise = False

-- Ejercicio 3
f3 :: [Integer] -> Integer -> [Integer]
f3 [] _ = []
f3 (x:xs) u | x < 0 = []
            | x <= u = x : f3 xs u
            | otherwise = u : f3 xs u

-- Ejercicio 4
f4 :: [[Integer]] -> Integer -> Integer
f4 [] _ = 0
f4 (x:xs) c | columnaEsPar x 1 c = 1 + f4 xs c
            | otherwise = f4 xs c

columnaEsPar :: [Integer] -> Integer -> Integer -> Bool
columnaEsPar (x:xs) i c | (i == c) = ((mod x 2) == 0)
                        | otherwise = columnaEsPar xs (i+1) c