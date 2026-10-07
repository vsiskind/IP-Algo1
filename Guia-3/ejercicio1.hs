double:: Int -> Int
double x = x + x

f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

h :: Integer -> Integer
-- fog
h num = f (g num)

k :: Integer -> Integer
-- gof
k num = f (g num)
