# problem7.py
SALARIO_BASE = 1423000  # COP

def evaluar_empleado(puntuacion: int):
    """
    Determina el nivel de rendimiento y la recompensa monetaria.
    Reglas:
    - 0              -> Inaceptable, recompensa = 0
    - 1 <= p <= 5    -> Aceptable, recompensa = SALARIO_BASE * p
    - p >= 6         -> Meritorio, recompensa = SALARIO_BASE * p
    - p < 0          -> Puntuación inválida
    """
    if puntuacion < 0:
        return "Puntuacion invalida", 0
    elif puntuacion == 0:
        return "Inaceptable", 0
    elif 1 <= puntuacion <= 5:
        return "Aceptable", SALARIO_BASE * puntuacion
    else:  # puntuacion >= 6
        return "Meritorio", SALARIO_BASE * puntuacion


if __name__ == "__main__":
    try:
        p = int(input("Ingrese la puntuacion del empleado (entero >=0): "))
        nivel, recompensa = evaluar_empleado(p)
        print(f"Nivel: {nivel}")
        print(f"Recompensa: ${recompensa:,} COP")
    except ValueError:
        print("Error: Debes ingresar un numero entero valido.")
