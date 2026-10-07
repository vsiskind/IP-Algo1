comparar :: Integer -> Integer -> Integer
comparar x y | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
             | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
             | otherwise = 0


sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = ((abs x) `mod` 10) + (((abs x) `div` 10) `mod` 10)