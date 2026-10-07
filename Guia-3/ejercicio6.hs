type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto a | a `mod` 4 /= 0 = False
           | (a `mod` 100 == 0) && (a `mod` 400 /= 0) = False
           | otherwise = True