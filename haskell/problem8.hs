-- problem8.hs

-- Escribe una funcion que tome la edad (age) como entrada
-- y devuelva el precio del ticket en funcion de los criterios especificados.
-- Categorias:
-- - 0 a 3 años     -> 0
-- - 4 a 12 años    -> 15000
-- - 13 a 17 años   -> 20000
-- - 18 a 64 años   -> 30000
-- - 65+ anos       -> 15000
-- Edad invalida (<0 o >120) -> -1 para indicar error

precioTicket :: Int -> Int
precioTicket edad
    | edad < 0 || edad > 120 = -1
    | edad <= 3   = 0
    | edad <= 12  = 15000
    | edad <= 17  = 20000
    | edad <= 64  = 30000
    | otherwise   = 15000

main :: IO ()
main = do
    putStrLn "Ingrese la edad del cliente: "
    entrada <- getLine
    let edad = read entrada :: Int
    let precio = precioTicket edad
    if precio == -1
        then putStrLn "Error: edad no valida."
        else putStrLn ("El precio del ticket es: $" ++ show precio ++ " COP")
