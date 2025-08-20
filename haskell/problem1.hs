-- Problem1.hs
module Problem1 (verificarEdad) where

verificarEdad :: Int -> String
verificarEdad edad
    | edad < 0        = "Error: edad no valida"
    | edad > 120      = "Error: edad no valida"
    | edad >= 18      = "Mayor de edad"
    | otherwise       = "Menor de edad"

-- funcion principal de prueba
main :: IO ()
main = do
    print (verificarEdad 20)    -- "Mayor de edad"
    print (verificarEdad 17)    -- "Menor de edad"
    print (verificarEdad (-5))  -- "Error: edad no valida"
    print (verificarEdad 150)   -- "Error: edad no valida"

