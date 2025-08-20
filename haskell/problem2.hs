-- Problem2.hs
module Problem2 (coincidePassword) where
import Data.Char (toLower)

-- Convierte una cadena a minusculas
aMinusculas :: String -> String
aMinusculas = map toLower

-- Compara contrasena guardada con la ingresada (sin distinguir mayusculas)
coincidePassword :: String -> String -> Bool
coincidePassword guardada entrada = aMinusculas guardada == aMinusculas entrada

-- funcion principal de prueba
main :: IO ()
main = do
    let guardada = "Magic2005"
    print (coincidePassword guardada "magic2005")   -- True
    print (coincidePassword guardada "Magic2005")   -- True
    print (coincidePassword guardada "MAGIC2005")   -- True
    print (coincidePassword guardada "Clave")       -- False
