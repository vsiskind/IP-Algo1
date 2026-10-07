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
contarPalabras :: String -> [[String]] -> Integer
contarPalabras _ [] = 0
contarPalabras p (x:xs) = contarPalabrasFilas p x + contarPalabras p xs

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