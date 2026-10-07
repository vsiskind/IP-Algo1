
estanRelacionados :: Integer -> Integer -> Bool
-- a*a + a*b*k = 0
--a*b*k = -a^2
--b*k = -a
--b*k = a
-- b es multiplo de a?
estanRelacionados a b = a `mod` b == 0
                      
