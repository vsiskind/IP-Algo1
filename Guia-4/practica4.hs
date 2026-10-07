-- Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

-- Ejercicio 2
parteEntera :: Float -> Integer
parteEntera x = truncate(x)

-- Ejercicio 3
esDivisible :: Integer -> Integer -> Bool
esDivisible a b = (modulo a b) == 0

modulo :: Integer -> Integer -> Integer
modulo x y
    | x < y = x
    | x >= y = modulo (x-y) y

-- Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = (2*n - 1) + sumaImpares (n - 1) 

-- Ejercicio 5
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n - 2)

-- Ejercicio 6
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n   | n < 10 = True 
                        | otherwise = (n `mod` 10) == ((n `div` 10) `mod` 10) && todosDigitosIguales (n `div` 10)

-- Ejercicio 7
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = (n `div` 10^(cantDigitos (n) - i)) `mod` 10

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = cantDigitos (n `div` 10) + 1

-- Ejercicio 8
sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = n `mod` 10 + sumaDigitos (n `div` 10)

-- Ejercicio 9
esCapicua :: Integer -> Bool 
esCapicua n | cantDigitos n == 1 = True
            | iesimoDigito n 1 ==  iesimoDigito n (cantDigitos n) = esCapicua((n `mod` 10 ^ ((cantDigitos n) - 1)) `div` 10) 
            | otherwise = False

-- Ejercicio 10
-- a)
f1 :: Integer -> Integer
-- requiere {n >= 0}
-- asegura {devuelve la sumatoria de i=0 a n de 2^i}
f1 n | n == 0 = 1
     | otherwise = 2 ^ n + f1 (n-1)

-- b)
f2 :: Integer -> Float -> Float
-- requiere {n >= 1}
-- asegura {devuelve la sumatoria de i=1 a n de q^i}
f2 n q | n == 1 = q
       | otherwise = q ^ n + f2 (n-1) q

-- c)
f3 :: Integer -> Float -> Float
-- requiere {n >= 1}
-- asegura {devuelve la sumatoria de i=1 a 2n de q^i}
f3 n q | n == 1 = q ^ 2 + q
       | otherwise = f2 (n*2) q

-- d)
f4 :: Integer -> Float -> Float
-- requiere {n >= 0}
-- asegura {devuelve la sumatoria de i=n a 2n de q^i}
f4 n q = f3 n q - f2 (n-1) q 

-- Ejercicio 11
-- a)
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = 1 / fromInteger (factorial n) + eAprox (n - 1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)

-- b)
e :: Float
e = eAprox 10

-- Ejercicio 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = raiz2 n - 1

raiz2 :: Integer -> Float
raiz2 1 = 2
raiz2 n = 2 + (1 / raiz2 (n-1))

-- Ejercicio 13
sumatoria :: Integer -> Integer ->  Integer
sumatoria n 1 = n
sumatoria n m = n ^ m + sumatoria n (m-1)

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 1 m  = sumatoria 1 m
sumatoriaDoble n m = sumatoria n m + sumatoriaDoble (n-1) m

-- Ejercicio 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q 1 m = sumatoriaN q 1 m
sumaPotencias q n m = sumatoriaN q n m + sumaPotencias q (n-1) m

sumatoriaN :: Integer -> Integer -> Integer -> Integer
sumatoriaN q n 1 = q^(n + 1)
sumatoriaN q n m = q^(n + m) + sumatoriaN q n (m-1)

-- Ejercicio 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m | n == 0 = 0
                   | otherwise = sumatoriaRac n m + sumaRacionales (n-1) m

sumatoriaRac :: Integer -> Integer -> Float
sumatoriaRac n m | m == 1 = fromInteger(n)
                 | otherwise = fromInteger(n) / fromInteger(m) + sumatoriaRac n (m-1)

-- Ejercicio 16
-- a)
menorDivisor :: Integer -> Integer
menorDivisor 1 = 1
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde d a | d `mod` a == 0 = a
                      | otherwise = menorDivisorDesde d (a+1)

-- b)
esPrimo :: Integer -> Bool
esPrimo p | p == 1 = False
          | otherwise = p == menorDivisor p

-- c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = mCD n m == 1

mCD :: Integer -> Integer -> Integer
mCD x y | y == 0 = x
        | otherwise = mCD y (x `mod` y)

-- d)
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = siguientePrimo (nEsimoPrimo (n-1))

siguientePrimo :: Integer -> Integer
siguientePrimo n | esPrimo (n+1) == True = n+1
                 | otherwise = siguientePrimo (n+1)

-- Ejercico 17

-- fibonacci :: Integer -> Integer
-- fibonacci 0 = 0
-- fibonacci 1 = 1
-- fibonacci n = fibonacci (n-1) + fibonacci (n-2)

esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux 0 n

esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux a n | fibonacci a > n = False
                     | fibonacci a == n = True
                     | otherwise = esFibonacciAux (a+1) n

-- Ejercicio 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | (cantDigitos n == 1) && not(esPar n) = -1
                 | (cantDigitos n == 1) && (esPar n) = n
                 | not(esPar (n `mod` 10)) = mayorDigitoPar(n `div` 10)
                 | esPar (n `mod` 10) = comparar (n `mod` 10) (mayorDigitoPar(n `div` 10))

esPar :: Integer -> Bool
esPar n = n `mod` 2 == 0

comparar :: Integer -> Integer -> Integer
comparar x y | x >= y = x
             | otherwise = y

-- Ejercicio 19
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n | n < 2 = False
                        | otherwise = sumaPrimosMayorQue n 2 2

sumaPrimosMayorQue :: Integer -> Integer -> Integer -> Bool
sumaPrimosMayorQue n p s | n == s = True 
                         | n > p = sumaPrimosMayorQue n (siguientePrimo p) (s + siguientePrimo p) 
                         | otherwise = False

-- Ejercicio 20
tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n1 n2 | n1 == n2 = n1
                   | otherwise = compararSuma n1 (tomaValorMax (n1+1) n2)

sumaDivisoresDesde :: Integer -> Integer -> Integer
sumaDivisoresDesde n a | a == n = a
                       | n `mod` a == 0 = a + sumaDivisoresDesde n (a+1)
                       | otherwise = sumaDivisoresDesde n (a+1)

compararSuma :: Integer -> Integer -> Integer
compararSuma x y | sumaDivisoresDesde x 1 >= sumaDivisoresDesde y 1 = x
                 | otherwise = y

-- Ejericio 21
pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r | n == 0 = sumaPita m 0 r
                | otherwise = sumaPita m n r + pitagoras m (n-1) r

sumaPita :: Integer -> Integer -> Integer -> Integer
sumaPita m n r | m == 0 && pitagorasValido m n r = 1
               | m == 0 = 0
               | pitagorasValido m n r = 1 + sumaPita (m-1) n r
               | otherwise = 0 + sumaPita (m-1) n r
              where pitagorasValido a b c = (a^2 + b^2) <= c^2