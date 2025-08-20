-- problem9.hs

-- Implementa una funcion que toma la eleccion del usuario
-- (vegetariana o no) y el ingrediente seleccionado,
-- devolviendo una descripcion de la pizza y si es vegetariana.

base :: [String]
base = ["mozzarella", "tomate"]

ingredientesVeget :: [String]
ingredientesVeget = ["Maiz tierno", "Platano maduro caramelizado", "Aguacate en laminas", "Queso costeno rallado"]

ingredientesNoVeget :: [String]
ingredientesNoVeget = ["Chorizo santarrosano", "Chicharron crocante", "Carne desmechada", "Pollo apanado con hogao"]

descripcionPizza :: Bool -> Int -> String
descripcionPizza esVeget opcion
    | opcion < 1 || opcion > length menu = "Error: opcion invalida"
    | otherwise = "Pizza " ++ tipo ++ " con " ++ ingredientesFinales
  where
    menu = if esVeget then ingredientesVeget else ingredientesNoVeget
    extra = menu !! (opcion - 1)
    tipo = if esVeget then "vegetariana" else "no vegetariana"
    ingredientesFinales = unwords (init (base ++ [extra])) ++ " y " ++ last (base ++ [extra])

main :: IO ()
main = do
    putStrLn "Desea una pizza vegetariana? (s/n): "
    r <- getLine
    let esVeget = map toLower r == "s"
    putStrLn "Seleccione un ingrediente adicional:"
    let menu = if esVeget then ingredientesVeget else ingredientesNoVeget
    mapM_ (\(i,ing) -> putStrLn (show i ++ ". " ++ ing)) (zip [1..] menu)
    opcionStr <- getLine
    let opcion = read opcionStr :: Int
    putStrLn (descripcionPizza esVeget opcion)
  where
    toLower c
        | c >= 'A' && c <= 'Z' = toEnum (fromEnum c + 32)
        | otherwise = c
