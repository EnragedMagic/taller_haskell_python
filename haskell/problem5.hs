-- Problem5.hs
module Problem5 (debePagarImpuestos) where

umbral :: Int
umbral = 53206000  -- COP

-- Funcion que determina si una persona debe pagar impuestos
debePagarImpuestos :: Int -> Int -> Bool
debePagarImpuestos edad ingresos =
    edad >= 18 && ingresos >= umbral

-- funcion principal de prueba
main :: IO ()
main = do
    print (debePagarImpuestos 25 60000000) -- True
    print (debePagarImpuestos 16 80000000) -- False
    print (debePagarImpuestos 30 50000000) -- False
    print (debePagarImpuestos 18 53206000) -- True
