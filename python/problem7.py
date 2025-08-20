# problem7.py
SALARIO_BASE = 2400000  # COP

def evaluar_empleado(puntuacion: float):
    """
    Determina el nivel de rendimiento y la recompensa en cuanto bonos.
    Reglas:
    - 0.0  -> Inaceptable, recompensa = 0
    - 0.4  -> Aceptable, recompensa = SALARIO_BASE * 0.4
    - >=0.6 -> Meritorio, recompensa = SALARIO_BASE * puntuacion
    - Otro -> Puntuación invakida 
    """
    if puntuacion == 0.0:
        return "Inaceptable", 0
    elif puntuacion == 0.4:
        return "Aceptable", int(SALARIO_BASE * 0.4)
    elif puntuacion >= 0.6:
        return "Meritorio", int(SALARIO_BASE * puntuacion)
    else:
        return "Puntuacion invalida", 0


if __name__ == "__main__":
    try:
        p = float(input("Ingrese la puntuacion del empleado: "))
        nivel, recompensa = evaluar_empleado(p)
        print(f"Nivel: {nivel}")
        print(f"Recompensa: ${recompensa:,} COP")
    except ValueError:
        print("Error: Debes ingresar un njmero valido (ej: 0.0, 0.4, 0.6).")
