-- Problem3.hs
module Problem3 (dividir) where

-- La funcion devuelve Either:
--   Right resultado si la division es valida
--   Left mensaje de error si el divisor es cero
dividir :: (Eq a, Fractional a) => a -> a -> Either String a
dividir _ 0 = Left "Error: division por cero"
dividir a b = Right (a / b)

-- funcion principal de prueba
main :: IO ()
main = do
    print (dividir 10 2)   -- Right 5.0
    print (dividir 7 0)    -- Left "Error: division por cero"
    print (dividir 5 2)    -- Right 2.5
