-- problem7.hs

-- Crea una funcion que toma una puntuacion y devuelve una tupla
-- con el nivel de rendimiento y el importe de la recompensa.
-- Reglas:
-- - 0              -> Inaceptable, recompensa = 0
-- - 1 <= p <= 5    -> Aceptable, recompensa = SALARIO_BASE * p
-- - p >= 6         -> Meritorio, recompensa = SALARIO_BASE * p
-- - p < 0          -> Puntuacion invalida

evaluarEmpleado :: Int -> (String, Int)
evaluarEmpleado p
    | p < 0     = ("Puntuacion invalida", 0)
    | p == 0    = ("Inaceptable", 0)
    | p >= 1 && p <= 5 = ("Aceptable", salarioBase * p)
    | otherwise = ("Meritorio", salarioBase * p)
  where
    salarioBase = 2400000

main :: IO ()
main = do
    putStrLn "Ingrese la puntuacion del empleado (entero >= 0): "
    entrada <- getLine
    let p = read entrada :: Int
    let (nivel, recompensa) = evaluarEmpleado p
    putStrLn ("Nivel: " ++ nivel)
    putStrLn ("Recompensa: $" ++ show recompensa ++ " COP")
