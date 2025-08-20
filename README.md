# Taller en Haskell y Python 
## Requisitos para correr en Python
**Python** 3.9 o superior.
- **GHC / GHCi** (Haskell Platform) 8.10 o superior.  
  Opcional: `runhaskell` para ejecutar sin compilar.
  cd haskell
## Requisitos para correr en Haskell
Entra a haskell/ y carga cada archivo en GHCi o ejecuta con runhaskell:
ghci Problem1.hs

## Descripción breve de cada problema (Python)

problem1.py — Verificador de edad legal
Verifica si la edad es mayor o menor de edad. Edad negativa o mayor a 120 → error.

problem2.py — Verificacion de contraseña (case-insensitive)
Compara con la contraseña almacenada ignorando mayúsculas/minúsculas.

problem3.py — Division con try/except
Divide dos números, manejando división por cero y entradas inválidas.

problem4.py — Par o impar
Determina si un número entero es par o impar. Entrada no entera → error.

problem5.py — Elegibilidad de impuestos
Mayor de edad y ingresos anuales >= 53,206,000 COP → paga impuestos.

problem6.py — Asignacion grupal
Grupo A: mujeres con inicial < 'M'; hombres con inicial >= 'N'.
Grupo B: resto.

problem7.py — Evaluacion de empleados

0 → Inaceptable.

1..5 → Aceptable (salario base × p).

>=6 → Meritorio (salario base × p).
Salario base = 1.423.000 COP.

problem8.py — Precios de Arcade

0–3: $0

4–12: $15,000

13–17: $20,000

18–64: $30,000

65+: $15,000

problem9.py — Pizza 
Vegetariana: Maiz tierno, Platano maduro caramelizado, Aguacate en laminas, Queso costeno rallado.
No vegetariana: Chorizo santarrosano, Chicharron crocante, Carne desmechada, Pollo apanado con hogao.
Base: mozzarella y tomate.






## Descripción breve de cada problema (Haskell)

Problem1.hs — Verificador de edad
verificarEdad :: Int -> String
Devuelve mayor/menor de edad o error si inválida.

Problem2.hs — Contraseña (case-insensitive)
coincidePassword :: String -> String -> Bool

Problem3.hs — División segura
dividir :: (Eq a, Fractional a) => a -> a -> Either String a

Problem4.hs — Par o impar
parOImpar :: Int -> String

Problem5.hs — Impuestos
debePagarImpuestos :: Int -> Int -> Bool

Problem6.hs — Asignación grupal
determinarGrupo :: String -> String -> String

Problem7.hs — Evaluación de empleados
evaluarEmpleado :: Int -> (String, Int)

Problem8.hs — Precios de Arcade
precioTicket :: Int -> Int

Problem9.hs — Pizza 
descripcionPizza :: Bool -> Int -> String

### Hecho por Johan Steven Galeano Gonzalez
