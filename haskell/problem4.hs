-- Problem4.hs
module Problem4 (parOImpar) where

-- Funcion que determina si un numero entero es par o impar
parOImpar :: Int -> String
parOImpar n
    | even n    = "Par"
    | otherwise = "Impar"

-- funcion principal de prueba
main :: IO ()
main = do
    print (parOImpar 4)    -- "Par"
    print (parOImpar 7)    -- "Impar"
    print (parOImpar 0)    -- "Par"
    print (parOImpar (-3)) -- "Impar"
