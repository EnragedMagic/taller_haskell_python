-- problem6.hs

-- Determina el grupo del estudiante segun su nombre y genero.
-- Mujeres: Grupo A si el nombre empieza con letra 'M' o anteriores.
-- Hombres: Grupo A si el nombre empieza con letra 'N' o posteriores.
-- El resto para el Grupo B.

import Data.Char (toUpper)

determinarGrupo :: String -> String -> String
determinarGrupo nombre genero
    | null nombre || null genero = "Error: datos invalidos."
    | generoNorm == "F" && inicial < 'M' = "Grupo A"
    | generoNorm == "M" && inicial >= 'N' = "Grupo A"
    | otherwise = "Grupo B"
  where
    inicial = toUpper (head (dropWhile (== ' ') nombre))
    generoNorm = [toUpper (head (dropWhile (== ' ') genero))]

main :: IO ()
main = do
    putStrLn "Ingrese su nombre: "
    nombre <- getLine
    putStrLn "Ingrese el genero que sale en su cedula (M o F): "
    genero <- getLine
    putStrLn ("Usted esta en el grupo: " ++ determinarGrupo nombre genero)

